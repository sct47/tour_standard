from django import forms

from .models import Player, Score, Course

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'world_ranking']
        labels = {'name': ''}

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['gross_score', 'date_played', 'course', ]
        labels = {'gross score': '', 'date played': '', }