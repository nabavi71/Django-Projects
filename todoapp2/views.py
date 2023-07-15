from django.shortcuts import render, redirect
from .models import TodoTask
from django.contrib.auth.decorators import login_required

from .models import TodoTask
from .forms import TodoTaskForm

def homeView(request):
    return render(request, 'todoapp2/home.html')

@login_required(login_url='/accunts/login')
def todoListView(request):
    user = request.user
    query = TodoTask.objects.filter(owner = user)
    if request.method == 'POST':
        checkedList = request.POST.getlist('checked')
        checkedList = [int(i) for i in checkedList]
        for todoItem in query:
            if todoItem.id in checkedList:
                TodoTask.objects.filter(id = todoItem.id).update(checked=True)
            else:
                TodoTask.objects.filter(id=todoItem.id).update(checked=False)
        return redirect('/list')
    return render(request, 'todoapp2/todo_list.html', {'todolist':query})

@login_required(login_url='/accunts/login')
def todoTaskCreate(request):
    user= request.user
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = user
            record.save()
            return redirect('todoapp2:todoList')
    form = TodoTaskForm()

    return render(request, 'todoapp2/create_todo_task.html', {'form':form})

@login_required(login_url='/accunts/login')
def todoTaskDelete(request, id):
    try:
        task = TodoTask.objects.get(id=id)
    except:
        return redirect('todoapp2:todoList')
    if task.owner == request.user:
        task.delete()
        return redirect('todoapp2:todoList')
    else:
        return redirect('todoapp2:todoList')
