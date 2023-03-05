from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.registerUser,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),  
    path('profileup',views.profileUpdate,name='profileup'),
    #path('profilesee',views.profile_see,name='profilesee'),
    path('pro1',views.pro1,name='pro1'),
    path('updateprof',views.updateprof,name='updateprof'),
    path('updateprof1',views.updateprof1,name='updateprof1'),
    path('updateprof2',views.updateprof2,name='updateprof2'),
    path('pro2',views.pro2,name='pro2'),
    path('pro3',views.pro3,name='pro3'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('chat',views.chat,name='chat'),
    path('dating',views.dating,name='dating')
]
