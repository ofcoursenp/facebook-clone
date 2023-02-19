from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DefineUser(models.Model):
    bio = models.CharField(max_length=300)
    profilePic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio


