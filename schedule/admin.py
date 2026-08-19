from django.contrib import admin

from .models import Member, Shift, ShiftPreference, Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["id", "name"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    fields = ["first_name", "last_name"]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "long_name",
        "description",
    ]


@admin.register(ShiftPreference)
class ShiftPreferenceAdmin(admin.ModelAdmin):
    list_display = [
        "member",
        "shift",
        "note",
        "date",
        "weekday",
    ]
