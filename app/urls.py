from django.urls import path
from . import views


urlpatterns = [
    path('top/', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login_form'),
    path('logout/',views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_view, name='register_view'),
    path('food_information/', views.food_information, name='food_information'),
]