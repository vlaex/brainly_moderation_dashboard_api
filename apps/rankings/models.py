from django.db import models
from django.conf import settings
from timescale.db.models.models import TimescaleModel


class ModeratorRanking(TimescaleModel):
    """
    Used for storing time-based data about the number of actions performed by a moderator
    within a specified timestamp on their respective market.
    """

    moderator = models.ForeignKey("moderators.Moderator", models.SET_NULL, null=True, blank=True)
    value = models.PositiveIntegerField()
    market = models.CharField(max_length=5, choices=settings.SUPPORTED_MARKETS)

    class Meta:
        db_table = "moderator_rankings"
