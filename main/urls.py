from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.landing,name='mainpage'),
    path('home',views.index,name='home'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('edit',views.edit,name='edit'),
    path('create',views.create,name='create'),
    path('user/<str:name>',views.viewUser,name='viewuser'),
    path('post/<int:post_id>',views.Like_post,name='viewpost'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('chat',views.chatPage,name='chat'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
