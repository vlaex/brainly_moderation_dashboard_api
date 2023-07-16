from django.db import models


class ModeratorHoliday(models.Model):
    """
    Represents a holiday or time off taken by a moderator.
    """

    id = models.AutoField(primary_key=True)
    moderator = models.ForeignKey("moderators.Moderator", on_delete=models.CASCADE, related_name="active_holidays")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    reason = models.CharField(max_length=255)

    class Meta:
        db_table = "moderator_holidays"
