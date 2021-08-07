from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_price = models.DecimalField(max_digits=12, decimal_places=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField()
    saved_listings = models.ManyToManyField(Listing)
    is_seller = models.BooleanField()

class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Message_sender')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Message_recipient')
    sent_time = models.DateTimeField()
    body = models.TextField()

