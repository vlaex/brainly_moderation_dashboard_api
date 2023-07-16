from django.db import models


class Achievement(models.Model):
    """
    Represents an achievement.

    Achievements can be awarded to moderators or teams of moderators
    to recognize their accomplishments or milestones.

    The points field specifies the number of points that will be awarded to a moderator or team
    upon achieving this particular achievement. Points are used for rankings, leaderboards, achievements.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    points = models.IntegerField()

    class Meta:
        db_table = "achievements"


class BaseAchievement(models.Model):
    """
    This abstract base model stores information about the achievement assignment.
    """

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    assigner_comment = models.TextField(blank=True)
    points = models.IntegerField()

    class Meta:
        abstract = True


class ModeratorAchievement(BaseAchievement):
    """
    Represents the assignment of an achievement to a moderator.
    """

    moderator = models.ForeignKey("moderators.Moderator", on_delete=models.CASCADE)
    assigner = models.ForeignKey(
        "moderators.Moderator",
        on_delete=models.CASCADE,
        related_name="moderator_achievement_assignments"
    )

    class Meta:
        db_table = "moderator_achievements"


class TeamAchievement(BaseAchievement):
    """
    Represents the assignment of an achievement to a team.
    """

    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE)
    assigner = models.ForeignKey(
        "moderators.Moderator",
        on_delete=models.CASCADE,
        related_name="team_achievement_assignments"
    )

    class Meta:
        db_table = "team_achievements"
