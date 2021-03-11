from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ProjectForm
from .models import Project

# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")


def log_in(request):
    # si l'utilisateur est déjà loggé: redirection sur la home
    if request.user.is_authenticated:
        return redirect('/app/', permanent=False)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # mettre l'utilisateur en session: redirection sur la home
            login(request, user)
            return redirect('/app/', permanent=False)
    return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect('/app/', permanent=False)


class ProjectView(FormView):
    template_name = 'new_project.html'
    form_class = ProjectForm
    success_url = '/app/projects'

    def form_valid(self, form):
        form.hash_token()
        data = form.cleaned_data
        data["slug"] = data["name"]
        p = Project(**data)
        p.save()
        return super().form_valid(form)


class ListProjectView(ListView):
    template_name = 'projects.html'
    model = Project
    paginate_by = 100


class DetailProjectView(DetailView):
    template_name = 'project.html'
    model = Project






