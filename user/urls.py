from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('check_user/', views.check_user, name="check_user"),
    path('add_user/', views.add_user, name="add_user"),
]