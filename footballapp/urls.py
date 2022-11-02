from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.TeamList.as_view(), name="list"),
    path("detail/<int:pk>/", views.TeamDetail.as_view(), name="detail"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("toggle_support_receive_team_status/", views.toggle_support_receive_team_status, name="toggle_support_receive_team_status"),
    path("myteamlist/", views.MyTeamList.as_view(), name="myteamlist"),
]
