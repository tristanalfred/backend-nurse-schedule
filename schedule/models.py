from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)


class Shift(models.Model):
    name = models.CharField(max_length=1, primary_key=True, unique=True)
    description = models.CharField(max_length=200)


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    prefered_shifts = models.ManyToManyField(Shift)
