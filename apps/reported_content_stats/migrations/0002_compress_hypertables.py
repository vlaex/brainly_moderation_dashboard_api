from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reported_content_stats", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL("""
        ALTER TABLE reported_content_stats SET (
            timescaledb.compress,
            timescaledb.compress_orderby = 'time DESC',
            timescaledb.compress_segmentby = 'market'
        );
        """),
        migrations.RunSQL("SELECT add_compression_policy('reported_content_stats', INTERVAL '8 weeks');")
    ]
