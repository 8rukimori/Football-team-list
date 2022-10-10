from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.TeamList.as_view(), name="list"),
    path("detail/<int:pk>/", views.TeamDetail.as_view(), name="detail"),
]
