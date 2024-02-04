from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def Todos(request):
    return render(request, 'Todo/tasks.html')
