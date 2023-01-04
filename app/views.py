from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    if request.method=="POST":
        task = request.POST['task']
        start = request.POST['start']
        finish = request.POST['finish']
        Todo.objects.create(task=task,start=start,finish=finish)
        return redirect('/')
    todos = Todo.objects.all()
    context = {
        "todos":todos
    }
    return render(request,"index.html",context=context)

def comuncom(request,id):
    task = Todo.objects.get(id=id)
    task.status = not(task.status)
    task.save()
    return redirect('/')

def deletetask(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect("/")

def updatetask(request,id):
    if request.method=="POST":
        task = request.POST['task']
        start = request.POST['start']
        finish = request.POST['finish']
        todo = Todo.objects.get(id=id)
        todo.task = task
        todo.start = start
        todo.finish = finish
        todo.save()
        return redirect('/')
    task = Todo.objects.get(id=id)
    context = {
        "task":task
    }
    return render(request,'update.html',context=context)