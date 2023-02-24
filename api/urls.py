from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.profile,name='apihome'),
    path('/user/<int:name>/', views.viewUser, name='viewUser'),
    path('/posts', views.index, name='viewpost'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
