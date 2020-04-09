from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('check_user/', views.check_user, name="check_user"),
    path('get_user/', views.get_user, name="get_user"),
    path('add_user/', views.add_user, name="add_user"),
    path('edit_user/', views.edit_user, name="edit_user"),
    path('del_user/', views.del_user, name="del_user"),
    path('get_user_trend/', views.get_user_trend, name="get_user_trend"),
    path('get_user_map/', views.get_user_map, name="get_user_map"),
]