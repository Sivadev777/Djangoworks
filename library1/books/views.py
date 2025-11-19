from idlelib.textview import ViewFrame

from django.shortcuts import render,redirect
from books.forms import addbooksform
from django.views import View


# Create your views here.
# def home(request):
#     return render(request, 'home.html')
# def addbooks(request):
#     return render(request, 'addbooks.html')
# def viewbooks(request):
#     return render(request, 'viewbooks.html')

class home(View):
    def get(self, request):
        return render(request, 'home.html')

class viewbooks(View):

    def get(self, request):
        b=Book.objects.all()
        context = {'books':b}
        return render(request, 'viewbooks.html',context)


from books.models import Book

class addbooks(View):
    def get(self, request):
        form_instance = addbooksform()
        context = {'form':form_instance}
        return render(request, 'addbooks.html',context)

    def post(self,request):
        #craeting from object using submitted data
        form_instance=addbooksform(request.POST,request.FILES)
        #check whether data is valid or not
        if form_instance.is_valid():

            #process the data after validation
            # data=form_instance.cleaned_data
            # # print('cleaned data',data)
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['page']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,page=pg,language=l)
            # b.save()
            form_instance.save()
        return render(request,'addbooks.html')

class Detailview(View):
    def get(self, request,i):
        b=Book.objects.get(id=i)
        context = {'book':b}
        return render(request, 'detail.html',context)

class Deleteview(View):
    def get(self, request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')

class Editview(View):
    def post(self, request,i):
        b=Book.objects.get(id=i)
        form_instance = addbooksform(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:addbooks')


    def get(self, request,i):
        b=Book.objects.get(id=i)
        from_instance=addbooksform(instance=b)
        context = {'form':from_instance}
        return render(request, 'edit.html',context)