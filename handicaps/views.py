from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import functools

from .models import Player, Course, Score
from .forms import PlayerForm, ScoreForm

def index(request):
    """The homepage for Handicap."""
    return render(request, 'handicaps/index.html')

def players(request):
    """Show all players."""
    players = Player.objects.order_by('world_ranking')
    context = {'players':players}
    return render(request, 'handicaps/players.html', context)

def player(request, player_id):
    """Show a single player and their details."""
    player = Player.objects.get(id=player_id)
    scores = player.score_set.order_by('-date_played')
    courses = Course.objects.all()
    played_to = []
    score_list = list(scores)
    for score in score_list[::-1]:
        played_to.append((score.gross_score-score.course.rating)*113/score.course.slope)
        last20 = played_to[:20]
        top8 = sorted(last20)[:8]
        score.handicap = round(((functools.reduce(lambda a,b : a+b, top8))/len(top8))*0.93, 1)
    context = {'player': player, 'scores': scores, 'courses': courses}
    return render(request, 'handicaps/player.html', context)

def courses(request):
    """Course Info page."""
    courses = Course.objects.order_by('id')
    context = {'courses': courses}
    return render(request, 'handicaps/courses.html', context)

def new_player(request):
    """Add a new player."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PlayerForm()

    else:
        # POST Data submitted; process data.
        form = PlayerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('handicaps:players'))

    context = {'form': form}
    return render(request, 'handicaps/new_player.html', context)

def new_score(request, player_id):
    """Add a new score for a player."""
    player = Player.objects.get(id=player_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ScoreForm()
    else:
        # POST data submitted; process data.
        form = ScoreForm(data=request.POST)
        if form.is_valid():
            new_score = form.save(commit=False)
            new_score.player = player
            new_score.save()
            return HttpResponseRedirect(reverse('handicaps:player', args=[player_id]))
    context = {'player': player, 'form': form}
    return render(request, 'handicaps/new_score.html', context)