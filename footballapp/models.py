from django.db import models
from django.conf import settings

class TeamModel(models.Model):
    team_name = models.CharField(max_length=256)
    headline = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hometown  = models.CharField(
        verbose_name="prefecture",
        choices=settings.PREFECTURES,
        max_length=26
        )
    clubhouse_location = models.CharField(max_length=256)
    established = models.DateField(default="1969-7-20")
    achievement = models.TextField(blank=True, null=True)
    headcoach = models.CharField(max_length=128, blank=True, null=True)
    headcoach_message = models.TextField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    featured_image = models.ImageField(
        default=None, 
        blank=True, 
        null=True, 
        upload_to=""
        )
    logo = models.ImageField(
        default=None, 
        blank=True, 
        null=True, 
        upload_to=""
        )
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.team_name

