from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Shift(models.Model):
    name = models.CharField(max_length=2, primary_key=True, unique=True)
    long_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)


class ShiftPreference(models.Model):
    class PreferenceScope(models.TextChoices):
        DEFAULT = "DEFAULT", "Default"
        WEEKDAY = "WEEKDAY", "Weekday"
        DATE = "DATE", "Date"
        
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="shift_preferences",
    )
    shift = models.ForeignKey(
        Shift,
        on_delete=models.CASCADE,
    )
    note = models.PositiveSmallIntegerField()
    date = models.DateField(
        null=True,
        blank=True,
    )
    weekday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    
    @property
    def scope(self):
        if self.date is not None:
            return self.PreferenceScope.DATE

        if self.weekday is not None:
            return self.PreferenceScope.WEEKDAY

        return self.PreferenceScope.DEFAULT
    
    class Meta:
        # date = None, weekday = None : default preference
        # date = None, weekday set : preference for a specific weekday
        # date set, weekday = None : preference for a specific date
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(date__isnull=True)
                    | models.Q(weekday__isnull=True)
                ),
                name="date_or_weekday_not_both",
            ),
        ]
