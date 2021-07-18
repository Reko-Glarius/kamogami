from django.db import migrations, models
import arrow

def add_default_days(apps, schema_editor):
    from calendario.models import days_name
    AttentionHoursModel = apps.get_model("calendario", "attention_hours")

    for day in days_name:
        AttentionHoursModel.objects.create(
            day=day[0],
            start_time=arrow.get('2021-01-01T09:00').time(),
            end_time=arrow.get('2021-01-01T19:00').time()
        )

def remove_default_days(apps, schema_editor):
    AttentionHoursModel = apps.get_model("calendario", "attention_hours")
    att_hours = AttentionHoursModel.objects.filter(valid_from=None, valid_until=None)
    if att_hours:
        att_hours.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_auto_20210718_1640'),
    ]

    operations = [
        migrations.RunPython(add_default_days, remove_default_days)
    ]