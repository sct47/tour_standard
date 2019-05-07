from django.contrib import admin

from handicaps.models import Player, Course, Score

admin.site.register(Player)
admin.site.register(Course)
admin.site.register(Score)