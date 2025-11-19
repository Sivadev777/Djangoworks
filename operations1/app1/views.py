from django.shortcuts import render
from django.views import View

from app1.forms import additionform,factorialform,bmiform,signupform



#CLASS BASED VIEWS
class addition(View):
    def get(self,request):
        form_instance=additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)
    def post(self,request):
        #craeting from object using submitted data
        form_instance=additionform(request.POST)
        #check whether data is valid or not
        if form_instance.is_valid():
            #process the data after validation
            data=form_instance.cleaned_data
            print('cleaned data',data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}
        return render(request,'addition.html',context)
class factorial(View):
    def get(self,request):
        form_instance=factorialform()
        context={'form':form_instance}
        return render(request,'factorial.html',context)
    def post(self,request):
        #craeting from object using submitted data
        form_instance=factorialform(request.POST)
        #check whether data is valid or not
        if form_instance.is_valid():
            #process the data after validation
            data=form_instance.cleaned_data
            print('cleaned data',data)
            n=data['num']

            fact=1
            for i in range(1,n+1):
                fact=fact*i


            context={'result':fact,'form':form_instance}
        return render(request,'factorial.html',context)

class bmi(View):
    def get(self, request):
        form_instance = bmiform()
        context={'form':form_instance}
        return render(request, 'bmi.html',context)

    def post(self, request):
        form_instance = bmiform(request.POST)
        context = {'form': form_instance}  # always define context

        if form_instance.is_valid():
            data = form_instance.cleaned_data
            h = data['height']
            w = data['weight']
            bmi = w / ((h / 100) ** 2)
            context={'result':bmi,'form':form_instance}
        return render(request, 'bmi.html',context)














class signup(View):
    def get(self,request):
        form_instance=signupform()
        context={'form':form_instance}
        return render(request,'signup.html',context)
    def post(self,request):
        form_instance=signupform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
        return render(request,'signup.html')