from django.urls import path
from album import views

urlpatterns = [
    path('get_album/', views.get_album),
    path('add_album/', views.add_album),
    path('add_index/', views.add_index),
    path('get_chapter/', views.get_chapter),
    path('get_index/', views.get_index),
    path('edit_index/', views.edit_index),
    path('del_index/', views.del_index),
]