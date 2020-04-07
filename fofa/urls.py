from django.urls import path
from fofa import views

app_name = 'fofa'

urlpatterns = [
    path('index/', views.index, name='index')
]
