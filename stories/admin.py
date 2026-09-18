from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    fields = ("title", "description", "image", "answer", "resolution_image")
    search_fields = ("title", "description", "answer")
    list_filter = ("created_at",)