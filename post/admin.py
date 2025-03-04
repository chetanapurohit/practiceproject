from django.contrib import admin
from .models import CustomUser, Post, Category


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_no', 'bio']

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Category)
# Register your models here.
