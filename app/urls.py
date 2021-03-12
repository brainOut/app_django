from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('new_project', login_required(views.ProjectView.as_view()), name="new_project"),
    path('projects', login_required(views.ListProjectView.as_view()), name="projects"),
    # path('project/<slug:slug>', login_required(views.DetailProjectView.as_view()), name="project"),
    path('project/<slug:slug>', views.project_details, name="project"),
]