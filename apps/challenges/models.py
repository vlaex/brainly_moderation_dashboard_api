from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


class BaseChallenge(models.Model):
    """
    Represents a base challenge.

    This abstract base model stores common fields and validation logic
    for challenges started by moderators and teams.
    """

    id = models.AutoField(primary_key=True)
    market = models.CharField(max_length=5, choices=settings.SUPPORTED_MARKETS)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    target_actions = models.PositiveIntegerField()
    bet = models.IntegerField()

    class Meta:
        abstract = True

    def clean(self):
        if self.end_date < timezone.now().date():
            raise ValidationError("Challenge end date should be in the future.")  # TODO: add validation

        if self.target_actions <= 0:
            raise ValidationError("Target actions should be a positive value.")


class ModeratorChallenge(BaseChallenge):
    """
    Represents a custom challenge started by a moderator.
    """

    moderator = models.ForeignKey("moderators.Moderator", on_delete=models.CASCADE, related_name="moderator_challenges")

    class Meta:
        db_table = "moderator_challenges"

    def clean(self):
        super().clean()

        if self.bet > 0:
            max_bet = int(self.moderator.points * 0.1)  # TODO: add some strategies of how many should moderator get points
            if self.bet > max_bet:
                raise ValidationError(f"Bet cannot exceed {max_bet} points.")

        elif self.bet < 0:
            if abs(self.bet) > self.moderator.points:
                raise ValidationError("Cannot bet more points than you have.")


class TeamChallenge(BaseChallenge):
    """
    Represents a custom challenge started by a team.
    """

    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE, related_name="team_challenges")

    class Meta:
        db_table = "team_challenges"

    def clean(self):
        super().clean()

        if self.bet > 0:
            max_bet = int(self.team.points * 0.1)
            if self.bet > max_bet:
                raise ValidationError(f"Bet cannot exceed {max_bet} points.")

        elif self.bet < 0:
            if abs(self.bet) > self.team.points:
                raise ValidationError("Cannot bet more points than you have.")
