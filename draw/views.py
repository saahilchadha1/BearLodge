# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def login(request):
    return render(request, 'draw/login.html')

def register(request):
    return render(request, 'draw/register.html')

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