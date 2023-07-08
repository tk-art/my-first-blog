from django.urls import path
from . import views


urlpatterns = [
    path('top/', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login_form'),
    path('profile/', views.profile, name='profile'),
]