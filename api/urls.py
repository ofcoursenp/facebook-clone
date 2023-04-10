from django.urls import path,include
from knox import views as knox_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.profile,name='apihome'),
    path('user/<int:name>/', views.viewUser, name='viewUser'),
    path('posts', views.index, name='viewpost'),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
