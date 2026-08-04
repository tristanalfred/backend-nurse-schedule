from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("members", views.member_list, name="member_list"),
    path("teams", views.team_list, name="team_list"),
    path("teams/<int:id>", views.team_detail, name="team_detail"),
]
