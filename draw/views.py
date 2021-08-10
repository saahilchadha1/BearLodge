# chat/views.py
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from draw.models import Listing, Profile
import requests

def index(request):
    return render(request, 'draw/index.html')

def login(request):
    return render(request, 'draw/login.html')

def register(request):
    return render(request, 'draw/register.html')

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
            print(request.POST)
            print(profile)
            print("Flipping saved: " + str(profile.saved_listings.filter(pk=listing_id)))
            if profile.saved_listings.filter(pk=listing_id):
                print("Removing")
                profile.saved_listings.remove(listing)
                # profile[0].save()
            else:
                print("Adding")
                profile.saved_listings.add(listing)
                # profile[0].save()
    profile = list(Profile.objects.filter(user=request.user))
    profile[0].refresh_from_db()
    print(profile[0].is_seller)
    print(listing.seller)
    print(profile[0].user)
    isSeller = False
    isSaved = False
    if (profile and listing.seller == profile[0].user):
        isSeller = True
    print(profile[0].saved_listings.filter(pk=listing_id))
    if list(profile and profile[0].saved_listings.filter(pk=listing_id)):
        isSaved = True
    print(listing.seller)
    print(isSeller)
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
    return render(request, 'draw/listing_edit.html')

def messages(request):
    return render(request, 'draw/messages.html')

def messages_chat(request, user_id):
    return render(request, 'draw/messages_chat.html')