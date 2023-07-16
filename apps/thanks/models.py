from django.db import models


class Thank(models.Model):
    """
    Represents a thank-you message from one moderator to another.

    Moderators can express gratitude and send points to other moderators.
    The sending of points is limited based on the sender's points and a configurable threshold.

    If a moderator has more than N points (specified in Django settings),
    they can send points, but no more than 5% of their total points.
    """

    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    attachment_url = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    to_moderator = models.ForeignKey("moderators.Moderator", models.CASCADE, null=True, related_name="received_thanks")
    from_moderator = models.ForeignKey("moderators.Moderator", models.CASCADE, null=True, related_name="sent_thanks")
    points = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "thanks"
