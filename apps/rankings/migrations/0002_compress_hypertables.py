from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rankings", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL("""
        ALTER TABLE moderator_rankings SET (
            timescaledb.compress,
            timescaledb.compress_orderby = 'time DESC',
            timescaledb.compress_segmentby = 'moderator_id'
        );
        """),
        migrations.RunSQL("SELECT add_compression_policy('moderator_rankings', INTERVAL '8 weeks');")
    ]
