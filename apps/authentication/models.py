from django.db import models


class Invite(models.Model):
    """
    Represents an invite for a moderator.

    This model stores information about an invite, including a unique code,
    the inviter (moderator who generated the invite), the moderator that should be invited,
    expiration date, whether the invite requires registration, and whether to notify about joins.
    It also tracks the joined users who have accepted the invite.
    """

    code = models.CharField(unique=True, max_length=255, db_index=True)
    inviter = models.ForeignKey("moderators.Moderator", null=True, on_delete=models.CASCADE, related_name="generated_invites")
    invitee = models.ForeignKey("moderators.Moderator", null=True, on_delete=models.CASCADE, related_name="received_invites")
    expires_at = models.DateField(blank=True, null=True)
    requires_registration = models.BooleanField()
    notify_about_joins = models.BooleanField()
    joined_users = models.ManyToManyField("moderators.Moderator", blank=True, related_name="accepted_invites")

    class Meta:
        db_table = "invites"


class OneTimeLoginCode(models.Model):
    """
    Represents a one-time login code.

    This model stores information about a one-time login code, including a unique code,
    the moderator associated with the code, the creation timestamp and expiration timestamp.
    """

    code = models.CharField(unique=True, max_length=255, db_index=True)
    moderator = models.ForeignKey("moderators.Moderator", null=True, on_delete=models.CASCADE, related_name="one_time_login_codes")
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "one_time_login_codes"
