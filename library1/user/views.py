from django.shortcuts import render
from django.views import View


# Create your views here.
# def register(request):
#     return render(request, "register.html")
# def login(request):
#     return render(request,"login.html")

class register(View):
    def get(self, request):
        return render(request, 'register.html')
class login(View):
    def get(self, request):
        return render(request, 'login.html')
