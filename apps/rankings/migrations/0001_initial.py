from django.db import migrations, models
from django.contrib.postgres.operations import CreateExtension
import django.db.models.deletion
import timescale.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("moderators", "0001_initial"),
    ]

    operations = [
        CreateExtension("timescaledb"),
        migrations.CreateModel(
            name="ModeratorRanking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("time", timescale.db.models.fields.TimescaleDateTimeField(interval="1 day")),
                ("value", models.PositiveIntegerField()),
                ("market", models.CharField(choices=[("US", "us"), ("RU", "ru")], max_length=5)),
                ("moderator", models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to="moderators.moderator")),
            ],
            options={
                "db_table": "moderator_rankings",
            },
        )
    ]
