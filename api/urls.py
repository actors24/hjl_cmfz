from django.urls import path

from api import views

urlpatterns = [
    path('first_page/', views.first_page),
    path('get_album_content/', views.get_album_content),
    path('register/', views.register),
    path('modify_user/', views.modify_user),
]