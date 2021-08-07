from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from draw.models import Listing, Profile, Message

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display=('seller', 'street_address')

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'is_seller')

class MessageAdmin(admin.ModelAdmin):
    list_display=('from_user', 'to_user', 'sent_time')

admin.site.register(Listing, ListingAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)