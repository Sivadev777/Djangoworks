from django.shortcuts import render,redirect
from movieapp.forms import MovieForm
from movieapp.models import Movie
from django.views import View





class home(View):
    def get(self, request):
        m = Movie.objects.all()
        context = {'movies': m}
        return render(request, 'home.html', context)


class addmovie(View):
    def post(self, request):
        form_instance = MovieForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return render(request, 'addmovie.html')

    def get(self, request):
        form_instance = MovieForm()
        context = {'form': form_instance}
        return render(request, 'addmovie.html', context)

class Detail(View):
    def get(self, request, i):
        m = Movie.objects.get(id=i)
        context = {'movie': m}
        return render(request, 'detail.html', context)

class Delete(View):
    def get(self, request, i):
        m = Movie.objects.get(id=i)
        m.delete()
        return redirect('home')

class Update(View):
    def post(self, request, i):
        m = Movie.objects.get(id=i)
        form_instance = MovieForm(request.POST, request.FILES, instance=m)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

    def get(self, request, i):
        m = Movie.objects.get(id=i)
        form_instance = MovieForm(instance=m)
        context = {'form': form_instance}
        return render(request, 'update.html', context)
