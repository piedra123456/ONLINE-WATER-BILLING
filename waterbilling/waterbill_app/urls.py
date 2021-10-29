from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('latestl/', views.latestl, name='latestl'),
    path('oldl/', views.oldl, name='oldl'),
    path('profile/', views.profile, name='profile'),
]
