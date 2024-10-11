from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
     path('', views.home, name='home'),                
    path('login/', views.login, name='login'),        
    path('signup/', views.signup, name='signup'),     
    path('landing/', views.landing, name='landing'),  
    path('logout/', views.signout, name='logout'), 
    path('userInfo/', views.userInfo, name='user_info'), 
    path('updateUserInfo/', views.update_user_info, name='update_user_info'),
    path('submit_maintenance_request/', views.submit_maintenance_request, name='submit_maintenance_request'),
]