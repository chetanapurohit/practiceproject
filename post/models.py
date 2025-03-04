from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # no seperate table created


class CustomUser(AbstractUser, TimeStamped):
    username = None
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_no = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(TimeStamped):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(TimeStamped):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(TimeStamped):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments = models.TextField()
