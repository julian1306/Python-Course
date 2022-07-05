from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class User_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_profile",blank=True, null=True)       #CASCADE RELACIONADO # o restrict  el related_name para poder user un user.user_profile
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image',null=True,default='default.jpg')

