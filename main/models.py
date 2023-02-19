from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DefineUser(models.Model):
    bio = models.CharField(max_length=300)
    profilePic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True,upload_to='post/images')
    created_on = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)


class follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    following = models.CharField(max_length=40)


# class Follow(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)


