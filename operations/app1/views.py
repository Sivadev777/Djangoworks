from django.shortcuts import render

def addition(request):
    if request.method == "GET":
        return render(request, 'addition.html')

    if request.method == "POST":
        print(request.POST)
        n1= request.POST.get('num1')
        n2= request.POST.get('num2')
        s=int(n1)+int(n2)
        print(s)

        contex={'result':s, 'n1':n1,'n2':n2}
        return render(request, 'addition.html',contex)
def factorial(request):
    if request.method == "GET":
        return render(request, "factorial.html")

    if request.method == "POST":
        print(request.POST)
        n = int(request.POST.get('num1'))
        f = 1
        for i in range(1, n + 1):
            f = f * i
        context = {'result': f, 'n': n}
        return render(request, 'factorial.html', context)

def bmi(request):
    if request.method == "GET":
        return render(request, "bmi.html")
    if (request.method == "POST"):
        print(request.POST)
        weight =int(request.POST.get('w'))
        height =int(request.POST.get('h'))
        bmi = weight/((height/100) ** 2)
        context = {'result': bmi,'weight':weight,'height':height}
        return render(request,  'bmi.html', context)
