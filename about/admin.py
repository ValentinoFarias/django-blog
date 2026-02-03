from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import About, Collaborate


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


@admin.register(Collaborate)
class CollaborateAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_on")
