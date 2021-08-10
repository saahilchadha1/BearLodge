from django.forms import ModelForm
from django.contrib.auth.models import User
from draw.models import Profile
from django.contrib.auth.hashers import make_password

class CreateLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']   

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class CreateIsSellerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["is_seller"]
        