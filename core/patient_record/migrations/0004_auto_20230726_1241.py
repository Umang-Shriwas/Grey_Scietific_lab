# Generated by Django 2.2 on 2023-07-26 07:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient_record', '0003_auto_20230726_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='doctor_id',
        ),
        migrations.AddField(
            model_name='department',
            name='doctor_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]