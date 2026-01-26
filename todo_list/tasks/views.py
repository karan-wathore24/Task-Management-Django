from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
def add_task(request):
    return render(request, "add_task.html")

@login_required(login_url="login_page")
def tasks(request):
    task = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, "tasks.html", {"task": task})

@login_required(login_url="login_page")
def delete(request,id):
    Task.objects.filter(id=id,user=request.user).delete()
    return redirect("tasks")





@login_required(login_url="login_page")
def addtask(request):
    if request.method == "POST":
        tt = request.POST['title']
        ds = request.POST['description']

        if tt and ds is not None:
            t = Task(title=tt, description=ds, user=request.user)
            t.save()
            messages.success(request, "Task is Added")
            return redirect("tasks")
        else:
            messages.error(request, "Fill the all fields ")
            return redirect("add_task")
    else:
        return redirect("add_task")

@login_required(login_url="login_page")
def mark_done(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect("tasks")

@login_required(login_url="login_page")
def update_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    return render(request, "update.html", {"task": task})

@login_required(login_url="login_page")
def upd_task(request, id):
    if request.method=="POST":
        tt=request.POST['title']
        ds = request.POST['description']

        if tt and ds:
            task = Task.objects.get(id=id, user=request.user)
            task.title = tt
            task.description = ds
            task.save()
            messages.success(request, "Task is Updated")
            return redirect("tasks")
        else:
            messages.error(request, "Fill all fields")
            return redirect("update_task", id=id)
    else:
        return redirect("tasks")
