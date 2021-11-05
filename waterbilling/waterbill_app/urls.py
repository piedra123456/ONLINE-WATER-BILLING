from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # login
    path('signin/', views.signinpage, name='signin'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name="logout"),
    path('log/', views.logpage, name="log"),


    #consumer
    path('consumer/<str:id>', views.consumerpage, name='consumer'),
    path('latestl/', views.latestpage, name='latestl'),
    path('oldl/', views.oldpage, name='oldl'),
    path('profile/<str:id>', views.profilepage, name='profile'),
    path('Announcements/', views.announcementspage, name='Announcements'),
    path('viewAnnouncements/', views.viewAnnouncementspage, name='viewAnnouncements'),


    #admin
    path('addAnnounce/', views.addpage, name='addAnnounce'),
    path('Announce/', views.announcepage, name='Announce'),
    path('viewAnnounce/', views.viewpage, name='viewAnnounce'),
    path('upAnnounce/', views.updatepage, name='upAnnounce'),
    path('delAnnounce/', views.deletepage, name='delAnnounce')



]
