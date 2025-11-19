from django.shortcuts import render
from django.views import View

from employees.forms import employeeform



# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
from employees.models import Employee

class employees(View):
    def get(self, request):
        f=employeeform()
        context = {"form":f}
        return render(request, 'employees.html', context)
    def post(self, request):
        f=employeeform(request.POST)
        if f.is_valid():
            f.save()
            return render(request,'employees.html')
