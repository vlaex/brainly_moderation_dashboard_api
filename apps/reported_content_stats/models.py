from django.db import models
from django.conf import settings
from timescale.db.models.models import TimescaleModel


class ReportedContentStats(TimescaleModel):
    """
    Used for storing time-based data about the number of reported content items
    in a specific subject within a specified market.
    """

    count = models.PositiveIntegerField()
    subject_id = models.PositiveIntegerField()
    market = models.CharField(max_length=5, choices=settings.SUPPORTED_MARKETS)

    class Meta:
        db_table = "reported_content_stats"
