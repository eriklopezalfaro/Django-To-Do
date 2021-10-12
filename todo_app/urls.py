from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_todo),
    path('delete/<int:todo_id>/', views.delete),
]