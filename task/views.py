from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

# Create your views here.
def get_tasks(request):
    data = {}
    form = TaskForm(request.POST or None)
    instance = Task.objects.all()
    data['tasks'] = instance
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('get')
    return render(request, 'task/list.html', data)

def update_task(request, pk):
    data = {}
    instance = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=instance)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('get')
    return render(request, 'task/update.html', data)

def delete_task(request, pk):
    data = {}
    instance = Task.objects.get(pk=pk)
    if instance:
        instance.delete()
        return redirect('get')
    return render(request, 'task/update.html', data)
