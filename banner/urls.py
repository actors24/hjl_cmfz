from django.urls import path
from banner import views

app_name = "banner"

urlpatterns = [
    path('check_banner/', views.check_banner, name="check_banner"),
    path('add_banner/', views.add_banner, name="add_banner"),
    path('get_one_banner/', views.get_one_nanner, name="get_one_banner"),
    path('del_banner/', views.del_banner, name="del_banner"),
    path('edit_banner/', views.edit_banner, name="edit_banner"),
]
