# from django.shortcuts import render
# from .models import Project

# # Create your views here.


# def projects(request):
#     projects = Project.objects.all()
#     return render(request, "project.html", {"projects": projects})


from django.shortcuts import render
from .models import Project, User


def index(request):
    return render(request, "base.html")


def project(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects": projects})


def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})
