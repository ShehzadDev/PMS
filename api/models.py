from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("manager", "Manager"),
        ("qa", "QA"),
        ("developer", "Developer"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="images/", null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("review", "Review"),
        ("working", "Working"),
        ("awaiting_release", "Awaiting Release"),
        ("waiting_qa", "Waiting QA"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Document(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to="documents/")
    version = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.title}"


class UserProfile(User):
    class Meta:
        proxy = True

    def get_profile(self):
        return self.profile


class TaskStatus(Task):
    class Meta:
        proxy = True

    def is_open(self):
        return self.status == "open"


class CommentAuthor(Comment):
    class Meta:
        proxy = True

    def get_author_name(self):
        return self.author.username
