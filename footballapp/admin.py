from django.contrib import admin
from .models import TeamModel, PlayerModel, MyTeam

admin.site.register(TeamModel)
admin.site.register(PlayerModel)
admin.site.register(MyTeam)
