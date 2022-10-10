from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models



class TeamList(ListView):
    template_name = "list.html"
    model = models.TeamModel

class TeamDetail(DetailView):
    template_name = "detail.html"
    model = models.TeamModel
    