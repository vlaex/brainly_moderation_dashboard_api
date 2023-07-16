# Generated by Django 4.2.2 on 2023-07-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("teams", "0001_initial"),
        ("moderators", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Competition",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField(blank=True)),
                ("market", models.CharField(choices=[("US", "us"), ("RU", "ru")], max_length=5)),
                ("private", models.BooleanField(default=False)),
                ("participants", models.ManyToManyField(related_name="competitions", to="moderators.moderator")),
                ("teams", models.ManyToManyField(related_name="competitions", to="teams.team")),
            ],
            options={
                "db_table": "competitions",
            },
        ),
    ]
