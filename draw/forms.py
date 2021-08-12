from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from draw.models import Listing, Profile
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

class CreateListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [ "street_address", "monthly_price", "description"]
        labels= {
            "street_address": "Address",
            "monthly_price": "Rent",
            "description": "Description",
        }
        widgets = {
            "street_address": forms.TextInput(attrs={"style": "width: 100%;"}),
            "monthly_price": forms.TextInput(attrs={"style": "width: 100%;"}),
            "description": forms.Textarea(attrs={"style": "width: 100%; height: 20vh;"}),
        }
        