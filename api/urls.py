from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="projects"),
    path("projects/", views.project, name="projects"),
    path("users/", views.users, name="users"),
]
