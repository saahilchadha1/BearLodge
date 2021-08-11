# chat/views.py
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from draw.models import Listing, Profile
import requests
from django.contrib import messages as flash_messages
from django.shortcuts import render
from draw.forms import CreateLoginForm, CreateUserForm, CreateIsSellerForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout #auth_login to avoid to shadowing since view name = login
from django.shortcuts import redirect
from draw.models import Profile
from django.contrib.auth.models import User

      
def index(request):
    if request.user.is_anonymous:
        return render(request, 'draw/index.html')
    profile = Profile.objects.get(user = request.user)
    if profile.is_seller:
        return redirect('listings')
    else:
        return redirect('explore')

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
            flash_messages.error(request, "Username or password is incorrect")
            return redirect('login')
    else:
        login_form = CreateLoginForm()
        context = {'login_form': login_form}

    return render(request, 'draw/login.html', context)

def logout(request):
    auth_logout(request)
    flash_messages.info(request, "Log out successful")
    return redirect('index')

def register(request):
    if request.method == 'POST':       
        user_form = CreateUserForm(request.POST)
        is_seller_form = CreateIsSellerForm(request.POST)

        if user_form.is_valid():
            email_get = user_form.cleaned_data.get('email')
            post_fix = email_get.split('@')
            if post_fix[1] != 'berkeley.edu':
                flash_messages.error(request, 'Email has to be Berkeley email')
                return redirect('register')
            try:
                User.objects.get(email=user_form.cleaned_data.get('email'))
            except User.DoesNotExist:
                # usage refer to https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for       
                user = user_form.save(commit=False)
                user.username = user.email
                user.set_password(user_form.cleaned_data.get('password')) # use set_password to set the password as raw data, if not, unrecognized version will be on database, which causes query failure
                user.save()
                profile = is_seller_form.save(commit=False)   
                profile.user = user 
                profile.save()
                flash_messages.success(request, 'Account created successfully')
                return redirect('login')    
            flash_messages.error(request, 'Email address exists')     
            return redirect('register')
        else:
            print(user_form.errors)
            return redirect('index')
    else:
        user_form = CreateUserForm()
        is_seller_form = CreateIsSellerForm()
        context = {'user_form': user_form, 'is_seller_form': is_seller_form}

    return render(request, 'draw/register.html', context)

def explore(request):
    def euclideanDistance(listing, queryLat, queryLong):
        return ((float(listing.latitude) - queryLat) ** 2) + ((float(listing.longitude) - queryLong) ** 2)
    listings = Listing.objects.all()
    if request.method == 'POST':
        response = requests.get("http://api.positionstack.com/v1/forward", 
            params={
                "access_key": "bcdcc39c43ee1cfcdd79d5da21acb0fe",
                "query": request.POST['searchQuery'],
                "region": "Berkeley, CA"
            }
        ).json()['data'][0]
        queryLat = response['latitude']
        queryLong = response['longitude']
        listings = sorted(list(listings), key= lambda listing: euclideanDistance(listing, queryLat, queryLong))
        return render(request, 'draw/explore.html', {'listings': listings})
    else:
        return render(request, 'draw/explore.html', {
            'listings': listings
            })

def listing_detail(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    profileQuery = Profile.objects.filter(user=request.user)
    if request.method == 'POST' and profileQuery.count() > 0:
        for profile in profileQuery:
            if profile.saved_listings.filter(pk=listing_id):
                profile.saved_listings.remove(listing)
            else:
                profile.saved_listings.add(listing)
    profile = list(Profile.objects.filter(user=request.user))
    profile[0].refresh_from_db()
    isSeller = False
    isSaved = False
    if (profile and listing.seller == profile[0].user):
        isSeller = True
    if list(profile and profile[0].saved_listings.filter(pk=listing_id)):
        isSaved = True
    return render(request, 'draw/listing_detail.html', {
        'listing': listing, 
        'isSeller': isSeller, 
        'isSaved': isSaved,
        'listingId': listing_id
        })

def saved(request):
    return render(request, 'draw/saved.html')

def listings(request):
    return render(request, 'draw/listings.html')

def listings_create(request):
    return render(request, 'draw/listings_create.html')

def listing_edit(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    print(listing)
    if request.method == "POST":
        print('POST request')
        form_data = request.POST
        print(form_data['address'])
        print(form_data['rent'])
        print(form_data)
        listing.street_address = form_data['address']
        listing.monthly_price = form_data['rent']
        listing.save()
        return redirect('listings')
    return render(request, 'draw/listing_edit.html', {
        'listing': listing
    })

def messages(request):
    return render(request, 'draw/messages.html')

def messages_chat(request, user_id):
    return render(request, 'draw/messages_chat.html')