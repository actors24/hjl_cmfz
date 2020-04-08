from django.urls import path
from fofa import views

app_name = 'fofa'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('get_phone_code/', views.get_phone_code, name='get_phone_code'),
    path('check_code/', views.check_code, name='check_code'),
]
