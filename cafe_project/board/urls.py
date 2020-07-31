from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.board_read, name="board_read"),
    path('read/<int:pk>', views.board_read_one, name="board_read_one"),
    path('create/', views.board_create, name="board_create"),
]
