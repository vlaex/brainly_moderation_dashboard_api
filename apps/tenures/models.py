from django.db import models


class Tenure(models.Model):
    """
    This model tracks the start and end dates of a moderator's tenure, indicating the period
    during which they have been actively involved as a moderator.
    """

    id = models.AutoField(primary_key=True)
    moderator = models.ForeignKey("moderators.Moderator", on_delete=models.CASCADE, related_name="tenures")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    end_reason = models.TextField()

    class Meta:
        db_table = "tenures"
