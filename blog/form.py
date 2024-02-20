from django.forms import ModelForm
from .models import Blogse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Blogform(ModelForm):
    
    class Meta:
        model=Blogse
        fields='__all__'

class Loginform(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2']