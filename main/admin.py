from django.contrib import admin
from .models import DefineUser,Post,follow,Like,Comment
# Register your models here.

admin.site.register(DefineUser)
admin.site.register(Post)
admin.site.register(follow)
admin.site.register(Like)
admin.site.register(Comment)

