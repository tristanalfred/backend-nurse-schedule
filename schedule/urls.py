from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teams", views.team_list, name="team_list"),
    path("teams/<int:id>", views.team_detail, name="team_detail"),
    path("members", views.member_list, name="member_list"),
    path("members/<int:id>/shifts", views.member_shift_list, name="member_shift_list"),
    path("shifts", views.shift_list, name="shift_list"),
]
