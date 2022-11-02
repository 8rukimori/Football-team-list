from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import TeamModel, MyTeam
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required


class TeamList(ListView):
    template_name = "list.html"
    model = TeamModel

class TeamDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("login")

    template_name = "detail.html"
    model = TeamModel

    def get_context_data(self,**kwargs):

        context = super().get_context_data()

        supported_team = TeamModel.objects.get(pk=self.kwargs["pk"])
        current_user = self.request.user
        exist_support_team = MyTeam.objects.filter(supporter=current_user, myteam=supported_team)

        if exist_support_team.exists():
            context["is_exist_support"] = "is_exist_support"
            return context
        else:
            pass

class Login(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("list")


class Logout(LogoutView):
    template_name = "logout.html"

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def toggle_support_receive_team_status(request):
    support_get_team = get_object_or_404(TeamModel, pk=request.POST["team_id"])
    new_supporter = request.user

    #Check existing relationship
    exist_support_team = MyTeam.objects.filter(supporter=new_supporter, myteam=support_get_team)
    
    #When no existing rel.
    if not exist_support_team.exists():
        MyTeam.objects.create(supporter=new_supporter, myteam=support_get_team)
    else:
        exist_support_team.delete()
    #前の画面のUrlの形に修正
    # return redirect('/userbloglist/' + str(send_user.id) + '/?user=' + request.POST["user_id"])
    return redirect("list")

class MyTeamList(ListView): 
    template_name = "myteam_list.html"

    def get_queryset(self):
        return MyTeam.objects.filter(supporter=self.request.user)