from django.views import View

from employees.models import Employee
from django import forms

class employeeform(forms.ModelForm):
    class Meta:
        model =Employee
        fields ="__all__"
