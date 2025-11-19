from django.shortcuts import render,redirect
from django.views import View

from user.forms import SignupForm
from django.contrib.auth import authenticate,login

# Create your views here.
# def register(request):
#     return render(request, "register.html")
# def login(request):
#     return render(request,"login.html")

class register(View):
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('user:userlogin')


    def get(self, request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request, 'register.html',context)

from user.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
class Userlogin(View):
    def post(self,request):
       form_instance = LoginForm(request.POST)
       if form_instance.is_valid():
        data = form_instance.cleaned_data
        u = data['username']
        p = data['password']
        user = authenticate(username=u, password=p)

        if user:  # if user exists
            login(request, user)  # adds the user into current sessions
            return redirect('books:home')
        else:  # if user does not exist
            messages.error(request, "Invalid credentials.")
            return redirect('user:userlogin')

    def get(self, request):
        form_instance = LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html', context)

class Userlogout(View):
    def get(self, request):
        logout(request)   #remove the user from the  current session
        return redirect('user:userlogin')