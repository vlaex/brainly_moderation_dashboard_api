from django.db import models
from django.conf import settings


class Competition(models.Model):
    """
    Represents a competition.

    Competitions are events where teams/moderators compete against each other
    within a specified timeframe. Competitions can involve all moderators, teams of participants
    or individual participants. Competitions can be either private or public.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    teams = models.ManyToManyField("teams.Team", related_name="competitions")
    participants = models.ManyToManyField("moderators.Moderator", blank=True, related_name="competitions")
    all_moderators = models.BooleanField(default=False, verbose_name="For all moderators")
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    market = models.CharField(max_length=5, choices=settings.SUPPORTED_MARKETS)
    private = models.BooleanField(default=False)

    winner_moderator = models.ForeignKey("moderators.Moderator", on_delete=models.SET_NULL, null=True, related_name="won_in_competitions")
    winner_team = models.ForeignKey("teams.Team", on_delete=models.SET_NULL, null=True, related_name="won_in_competitions")

    class Meta:
        db_table = "competitions"
