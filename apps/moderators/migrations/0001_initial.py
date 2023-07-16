import django.contrib.postgres.fields
import django.core.validators
from django.contrib.postgres.operations import CryptoExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("achievements", "0001_initial"),
    ]

    operations = [
        CryptoExtension(),
        migrations.CreateModel(
            name="Moderator",
            fields=[
                ("global_id", models.CharField(db_column="id", primary_key=True, serialize=False, verbose_name="global_id")),
                ("user_id", models.BigIntegerField(verbose_name="id")),
                ("market", models.CharField(choices=[("US", "us"), ("RU", "ru")], max_length=5)),
                ("is_bot", models.BooleanField(default=False)),
                ("nick", models.CharField(db_index=True, max_length=30, validators=[django.core.validators.RegexValidator(message="Invalid nick", regex="^[\\w\\d]{,30}$")])),
                ("name", models.CharField(max_length=100, blank=True)),
                ("ranks", django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ("joined_at", models.DateTimeField(auto_now_add=True)),
                ("is_hidden", models.BooleanField(default=False)),
                ("is_deactivated", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(null=True)),
                ("avatar", models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.URLValidator(schemes=["https"])])),
                ("gender", models.CharField(choices=[("MALE", 1), ("FEMALE", 2), ("NON_BINARY", 3)], max_length=50)),
                ("date_of_birth", models.DateField(null=True)),
                ("helped_users_count", models.IntegerField(default=0)),
                ("thanks_from_users", models.IntegerField(default=0)),
                ("country", models.CharField(blank=True, max_length=5, null=True)),
                ("registered_at", models.DateTimeField(null=True)),
                ("password", models.TextField(blank=True, null=True)),
                ("last_active", models.DateField(null=True)),
                ("achievements", models.ManyToManyField(related_name="moderators", to="achievements.achievement")),
                ("friends", models.ManyToManyField(blank=True, to="moderators.moderator")),
                ("mentor", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="mentees", to="moderators.moderator")),
                ("groups", models.ManyToManyField(blank=True, help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.", related_name="user_set", related_query_name="user", to="auth.group", verbose_name="groups")),
                ("user_permissions", models.ManyToManyField(blank=True, help_text="Specific permissions for this user.", related_name="user_set", related_query_name="user", to="auth.permission", verbose_name="user permissions")),
                ("is_admin", models.BooleanField(default=False)),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
            ],
            options={
                "db_table": "moderators",
            },
        ),
        migrations.CreateModel(
            name="ModeratorSettings",
            fields=[
                ("moderator", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name="personalized_settings", serialize=False, to="moderators.moderator")),
                ("hide_date_of_birth", models.BooleanField(default=False)),
                ("hide_friends", models.BooleanField(default=False)),
                ("send_invite_to_mentees_automatically", models.BooleanField(default=False)),
                ("invite_to_mentees_expiration_days", models.PositiveIntegerField(default=0)),
                ("receive_mentee_notification", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "moderator_personalized_settings",
            }
        ),
    ]
