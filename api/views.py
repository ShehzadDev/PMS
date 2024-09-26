from django.shortcuts import render
from .models import (
    Project,
    User,
    Profile,
    Document,
    Task,
    Comment,
    UserProfile,
    TaskStatus,
    CommentAuthor,
)
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from django.db.models import Count
from django.db.models import Case, When, IntegerField
from django.db.models import F


def index(request):
    return render(request, "base.html")


def project(request):
    projects = Project.objects.all()

    return render(request, "project.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()

    return render(request, "tasks.html", {"tasks": tasks})


def users(request):

    users = User.objects.filter(
        email__in=["shakaibaziz98@gmail.com", "shehzadshifa@gmail.com"]
    )

    # users = User.objects.filter(email__icontains="shehzad")

    # users = User.objects.filter(email__isnull=False)

    # users = User.objects.filter(date_joined__lte=timezone.now())

    # users = User.objects.filter(date_joined__gte=datetime(2024, 9, 25))

    # isExist = User.objects.filter(email="shehzadshifa@gmail.com").exists()

    # users = User.objects.exclude(email="shehzadshifa@gmail.com")

    # dicttionay = User.objects.aggregate(total_users=Count("id"))

    # print(dicttionay)

    # users = User.objects.select_related("profile").all()

    # users = User.objects.prefetch_related("profile").all()

    # users = User.objects.all().order_by("username")

    # # users = User.objects.filter(username="alishehzad")

    # # users = User.objects.filter(Q(first_name="Shehzad") | Q(last_name="Shehzad"))

    # # users = User.objects.filter(email__icontains="shehzadshifa@gmail.com")

    # # users = User.objects.filter(email__endswith="i2cinc.com")

    # # users = User.objects.filter(email__startswith="shehzad")

    # # users = User.objects.filter(email__contains="shehzad")

    # # users = User.objects.filter(date_joined__lt=timezone.now())

    # # users = User.objects.all().order_by("username")

    # # users = User.objects.filter(date_joined__gte=datetime(2024, 9, 25))

    # # users = User.objects.exclude(email="shehzadshifa@gmail.com")

    # # users = User.objects.distinct()

    # # users = User.objects.all().reverse()

    # r1 = User.objects.filter(email="maziz@i2cinc.com")
    # r2 = User.objects.filter(email="shehzadshifa@gmail.com")

    # users = r1.union(r2)
    # # users = r1.intersection(r2)
    # # users = r1.difference(r2)

    user = User.objects.get(email="shakaibaziz98@gmail.com")

    count = User.objects.count()

    # users = User.objects.filter(Q(first_name="Shehzad") | Q(last_name="Shehzad"))

    # User.objects.filter(email="shehzadshifa@gmail.com").update(first_name="Shehzad")

    # User.objects.filter(email="ajawad@yahoo.com").delete()

    # User.objects.create(username="newuser", email="newuser@example.com").save()

    # User.objects.bulk_create(
    #     [
    #         User(username="support1", email="s1@managepro.com"),
    #         User(username="support2", email="s2@managepro.com"),
    #     ]
    # )

    # user, created = User.objects.get_or_create(
    #     username="help", defaults={"email": "help@managepro.com"}
    # )

    # user, created = User.objects.update_or_create(
    #     username="help", defaults={"email": "help1@managepro.com"}
    # )

    rcount = users.count()

    return render(
        request,
        "users.html",
        {"users": users, "count": count, "rcount": rcount, "user": user},
    )
