from django.db import models
from django.contrib.auth.models import User
# Import User model

class Registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # models.OneToOneField means that a registration belong to one owner and one owner has only one registration
    # models.CASCADE means once you delete the user you also delete the registration belong to that user as well
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='registration_logo/', blank=False)
    # It means registration must have a logo
    # To user ImageField we need to install Pillow
    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    # avatar is the link of the image url
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()
        # get_full_name is the function from User model from django


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()
