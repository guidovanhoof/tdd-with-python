from django.urls import path

from lists import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
    path('lists/<int:list_id>/create/', views.create_list, name='create_list'),
    path('lists/new/', views.new_list, name='new_list'),
]
