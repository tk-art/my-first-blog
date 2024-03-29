from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login_form'),
    path('logout/',views.logout_view, name='logout_view'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('register/', views.register_view, name='register_view'),
    path('notification/', views.notification, name='notification'),
    path('api/notifications/check', views.check_new_notifications, name='check_new_notifications'),
    path('food_information/<int:item_id>', views.food_information, name='food_information'),
    path('like_item/<int:item_id>/', views.like_item, name='like_item'),
    path('get_like_status/<int:item_id>/', views.get_like_status, name='get_like_status'),
    path('comment_item/<int:item_id>/', views.comment_item, name='comment_item'),
    path('search_category/', views.search_category, name='search_category'),
    path('search/', views.search, name='search'),
    path('want/<int:item_id>/', views.want, name='want'),
    path('message/<int:item_id>/', views.message, name='message'),
    path('button_click', views.button_click, name='button_click'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)