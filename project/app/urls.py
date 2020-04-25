
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # name='home'),
    path('add/', views.add), # name='add_todo'),
    path('delete/<int:contact_id>/', views.delete),
    path('details/<int:contact_id>/', views.details),
]








