from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'