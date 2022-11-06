from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeamList.as_view(), name="list"),
    path("detail/<int:pk>/", views.TeamDetail.as_view(), name="detail"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("toggle_support_receive_team_status/", views.toggle_support_receive_team_status, name="toggle_support_receive_team_status"),
    path("myteamlist/", views.MyTeamList.as_view(), name="myteamlist"),
    path("tokyo/", views.TokyoList.as_view(), name="list-tokyo"),
    path("osaka/", views.OsakaList.as_view(), name="list-osaka"),
    path("aichi/", views.AichiList.as_view(), name="list-aichi"),
    path("others/", views.OthersList.as_view(), name="list-others"),
]
