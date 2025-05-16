"""
URL patterns for the exercises app.
"""
from django.urls import path
from exercises import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('comment/<int:exercise_id>/', views.add_comment, name='add_comment'),
    path('list/', views.exercise_list, name='exercise_list'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('upload/<int:exercise_id>/', views.upload_media, name='upload_media'),
]