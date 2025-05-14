from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('comment/<int:exercise_id>/', views.add_comment, name='add_comment'),
    path('list/', views.exercise_list, name='exercise_list'),
    path('flashcards/', views.flashcards, name='flashcards'),
]