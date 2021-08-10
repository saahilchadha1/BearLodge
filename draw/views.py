# chat/views.py
from django.contrib import messages as flash_messages
from django.shortcuts import render
from draw.forms import CreateLoginForm, CreateUserForm, CreateIsSellerForm
from django.contrib.auth import authenticate, login as auth_login, logout #auth_login to avoid to shadowing since view name = login
from django.shortcuts import redirect
from draw.models import Profile
from django.contrib.auth.models import User

      
def index(request):
    return render(request, 'draw/index.html')

def login(request):
    if request.method == 'POST':
        login_form = CreateLoginForm(request.POST)

        # check if the user exists, if not, redirect to register
        cur_user = authenticate(request, username = login_form.data.get('username'), password = login_form.data.get('password'))
        profile = Profile.objects.get(user = cur_user) if cur_user is not None else None# authenticate only return user object, profile is needed next
        print(login_form.data.get('password'))
        if profile is not None:
            auth_login(request, cur_user)
            print(profile.is_seller)
            if profile.is_seller:
                return redirect('listings')
            else:
                return redirect('explore')
        else:
            flash_messages.info(request, "Username or password is incorrect")
            return redirect('login')
    else:
        login_form = CreateLoginForm()
        context = {'login_form': login_form}

    return render(request, 'draw/login.html', context)


def register(request):
    if request.method == 'POST':       
        user_form = CreateUserForm(request.POST)
        is_seller_form = CreateIsSellerForm(request.POST)

        if user_form.is_valid(): 
            match = User.objects.get(email=user_form.cleaned_data.get('email'),)
            if match is not None:
                flash_messages.error(request, 'Email address exists')     
                return redirect('register')
        
            # usage refer to https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for       
            user = user_form.save(commit=False)
            user.username = user.email
            user.set_password(user_form.cleaned_data.get('password')) # use set_password to set the password as raw data, if not, unrecognized version will be on database, which causes query failure
            user.save()
            profile = is_seller_form.save(commit=False)   
            profile.user = user 
            profile.save()
            flash_messages.info(request, 'Account created successfully')
            return redirect('login')
        else:
            print(user_form.errors)
            return redirect('index')
    else:
        user_form = CreateUserForm()
        is_seller_form = CreateIsSellerForm()
        context = {'user_form': user_form, 'is_seller_form': is_seller_form}

    return render(request, 'draw/register.html', context)

def explore(request):
    return render(request, 'draw/explore.html')

def listing_detail(request, listing_id):
    return render(request, 'draw/listing_detail.html')

def saved(request):
    return render(request, 'draw/saved.html')

def listings(request):
    return render(request, 'draw/listings.html')

def listings_create(request):
    return render(request, 'draw/listings_create.html')

def listing_edit(request, listing_id):
    return render(request, 'draw/listing_edit.html')

def messages(request):
    return render(request, 'draw/messages.html')

def messages_chat(request, user_id):
    return render(request, 'draw/messages_chat.html')