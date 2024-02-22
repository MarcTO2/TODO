from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Todo.models import Tasks

@login_required
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        # Handling the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(title, description)
        ins = Tasks(taskTitle=title, taskDescription=description, user=request.user)  # Associate task with current user
        ins.save()
        context = {'success': True}
    return render(request, 'base.html', context)

@login_required
def Todos(request):
    allTasks = Tasks.objects.filter(user=request.user)  # Filter tasks by current user
    context = {'tasks': allTasks}
    return render(request, 'Todo/tasks.html', context)

@login_required
def edit_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if task.user != request.user:  # Check if the task belongs to the current user
        return HttpResponse("You don't have permission to edit this task.")
    
    context = {'task': task}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.taskTitle = title
        task.taskDescription = description
        task.save()
        return redirect('Todos')
    return render(request, 'Todo/edit_task.html', context)

@login_required
def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if task.user != request.user:  # Check if the task belongs to the current user
        return HttpResponse("You don't have permission to delete this task.")
    
    task.delete()
    return redirect('Todos')

@login_required
def search_tasks(request):
    query = request.GET.get('q')
    if query:
        tasks = Tasks.objects.filter(user=request.user, taskTitle__icontains=query)  # Filter tasks by current user and search by task title
    else:
        tasks = Tasks.objects.filter(user=request.user)  # Filter tasks by current user
    context = {'tasks': tasks}
    return render(request, 'Todo/tasks.html', context)

@login_required
def update_task_completion(request, task_id):
    if request.method == 'POST':
        task = Tasks.objects.get(pk=task_id)
        task.complete = not task.complete  # Toggle completion status
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

