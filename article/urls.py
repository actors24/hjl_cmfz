from django.urls import path
from article import views

urlpatterns = [
    path('upload_pic/', views.upload_pic),
    path('get_article/', views.get_article),
    path('get_all_img/', views.get_all_img),
    path('add_article/', views.add_article),
    path('edit_article/', views.edit_article),
    path('del_article/', views.del_article),
]