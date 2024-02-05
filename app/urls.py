from django.urls import path
from .views import user_list, add_user, delete_user, user_profile, image

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/delete/<str:name>/', delete_user, name='delete_user'),
    path('users/profile/<str:name>/', user_profile, name='user_profile'),
    path('image/', image, name='image'),
]
