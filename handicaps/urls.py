"""Defines URL patterns for Handicap."""

from django.urls import path

from . import views

app_name = 'handicaps'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Players
    path('players/', views.players, name='players'),
    # Single Player
    path('players/<int:player_id>/', views.player, name='player'),
    # Page for adding a new player
    path('new_player/', views.new_player, name='new_player'),
    # Courses
    path('courses/', views.courses, name='courses'),
    # Page for adding a new score
    path('new_score/<int:player_id>/', views.new_score, name='new_score')

]
