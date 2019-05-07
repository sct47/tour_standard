from django.db import models

class Player(models.Model):
    """A player with a handicap"""
    name = models.CharField(max_length=200)
    world_ranking = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Course(models.Model):
    """List of Courses in play on the PGA Tour"""
    name = models.CharField(max_length=60)
    event = models.CharField(max_length=100)
    par =  models.IntegerField()
    rating = models.FloatField()
    slope = models.IntegerField()

    def __str__(self):
        """Return a String represenation of the model."""
        return self.name


class Score(models.Model):
    """Scores for each Player."""
    gross_score = models.IntegerField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    date_played = models.DateField(auto_now_add=False)
    

    def __str__(self):
        """String Representation."""
        return str(self.gross_score)