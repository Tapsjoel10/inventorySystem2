from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('logout/', views.logout_view, name='user-logout'),
    path('', views.loginView, name='user-login'),
    path('profile/', views.profile, name='user-profile'),
    path('profile/update', views.profileUpdate, name='user-profileUpdate'),
]