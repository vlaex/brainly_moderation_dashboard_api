# Generated by Django 4.2.2 on 2023-07-07 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("moderators", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tenure",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("start_date", models.DateField(auto_now_add=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("moderator", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="tenures", to="moderators.moderator")),
            ],
            options={
                "db_table": "tenures",
            },
        ),
    ]