from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from .forms import TodoForm,AddTodoForm


class Home(View):
    def get(self, request):
        form_instance = AddTodoForm()
        tasks = Todo.objects.all()
        context = {
            'form': form_instance,
            'tasks': tasks
        }
        return render(request, 'home.html', context)

    def post(self, request):
        form_instance = AddTodoForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('home')


class Add(View):
    def get(self, request):
        form_instance = AddTodoForm()
        context = {'form': form_instance}
        return render(request, 'add.html', context)

    def post(self, request):
        form_instance = AddTodoForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('home')


class Delete(View):
    def get(self, request, i):
        task = Todo.objects.get(id=i)
        task.delete()
        return redirect('home')


class Edit(View):
    def get(self, request, i):
        task = Todo.objects.get(id=i)
        form_instance = TodoForm(instance=task)
        context = {'form': form_instance, 'task': task}
        return render(request, 'edit.html', context)

    def post(self, request, i):
        task = Todo.objects.get(id=i)
        form_instance = TodoForm(request.POST, instance=task)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
        context = {'form': form_instance, 'task': task}
        return render(request, 'edit.html', context)