from django.contrib import admin

from .models import Member, Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["id", "name"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    fields = ["first_name", "last_name"]
