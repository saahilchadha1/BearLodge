# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('explore', views.explore, name='explore'),
    path('explore/<int:listing_id>', views.listing_detail, name='listing_detail'),
    path('saved', views.saved, name='saved'),
    path('listings', views.listings, name='listings'),
    path('listings/create', views.listings_create, name='listings_create'),
    path('listing/<int:listing_id>', views.listing_edit, name='listings_edit'),
    path('messages', views.messages, name='messages'),
    path('messages/<int:user_id>', views.messages_chat, name='messages_chat'),
]
