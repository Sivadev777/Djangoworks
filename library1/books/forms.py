from django import forms

from books.models import Book


# class addbooksform(forms.Form):
#     Title=forms.CharField()
#     Author=forms.CharField()
#     Price=forms.IntegerField()
#     Pages=forms.IntegerField()
#     Language=forms.CharField()

class addbooksform(forms.ModelForm): #define the form based on book model

    class Meta:  #innerclass used to define the structure of form.
        model = Book
        fields='__all__'