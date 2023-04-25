from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]