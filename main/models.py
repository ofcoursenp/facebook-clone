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
    like_from = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)


class follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    following = models.CharField(max_length=40)

    def __str__(self):
        return self.following

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField(max_length=999)
    
class Chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    seeing = models.CharField(max_length=50)
    chatting = models.TextField(max_length=999)

