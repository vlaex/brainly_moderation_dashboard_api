from django.db import models
from django.conf import settings
from django.core.validators import URLValidator


class Team(models.Model):
    """
    Represents a team.

    A team consists of moderators as members, with one or more leaders.
    Achievements can be assigned to teams.

    The `points` field indicates the number of points the team has.
    The point system is used for rankings and achievements.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    members = models.ManyToManyField("moderators.Moderator", related_name="teams")
    leaders = models.ManyToManyField("moderators.Moderator", on_delete=models.SET_NULL, blank=True, related_name="led_teams")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    market = models.CharField(max_length=5, choices=settings.SUPPORTED_MARKETS)
    logo = models.CharField(
        max_length=255,
        blank=True,
        validators=[URLValidator(["https"])],
        default=settings.DEFAULT_TEAM_LOGO_URL
    )
    points = models.IntegerField()

    achievements = models.ManyToManyField(
        "achievements.Achievement",
        through="achievements.TeamAchievement",
        related_name="assigned_to_teams"
    )

    class Meta:
        db_table = "teams"
