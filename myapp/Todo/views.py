from django.shortcuts import render, HttpResponse, redirect
from Todo.models import Tasks

# Create your views here.
def home(request):
    context = { 'success': False}
    if request.method == 'POST':
        # Handling the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(title, description)
        ins = Tasks(taskTitle=title, taskDescription=description)
        ins.save()
        context = { 'success': True}
        

    return render(request, 'base.html', context)

def Todos(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'Todo/tasks.html', context)

def edit_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    context = {'task': task}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.taskTitle = title
        task.taskDescription = description
        task.save()
        return redirect('Todos')  # Redirect to Todos view after editing

    return render(request, 'Todo/edit_task.html', context)

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('Todos')  # Redirect to Todos view after deletion

def search_tasks(request):
    query = request.GET.get('q')
    if query:
        tasks = Tasks.objects.filter(taskTitle__icontains=query)  # Search by task title (case-insensitive)
    else:
        tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'Todo/tasks.html', context)
