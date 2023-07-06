from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login_form'),
    path('logout/',views.logout_view, name='logout_view'),

    path('profile/', views.profile, name='profile'),
    path('register/', views.register_view, name='register_view'),
    path('notification/', views.notification, name='notification'),

    path('food_information/<int:item_id>', views.food_information, name='food_information'),
    path('like_item/<int:item_id>/', views.like_item, name='like_item'),
    path('comment_item/<int:item_id>/', views.comment_item, name='comment_item'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)