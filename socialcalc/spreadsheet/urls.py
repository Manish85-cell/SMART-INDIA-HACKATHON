from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_spreadsheet, name='create_spreadsheet'),
    path('<int:spreadsheet_id>/', views.spreadsheet_detail, name='spreadsheet_detail'),
    path('<int:spreadsheet_id>/update_cell/', views.update_cell, name='update_cell'),
    path('login', views.login_view, name = "login"),
    path('register', views.register, name = "register"),
    path('', views.index, name = "index"),
]