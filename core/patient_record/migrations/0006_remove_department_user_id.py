# Generated by Django 2.2 on 2023-07-26 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_record', '0005_auto_20230726_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='user_id',
        ),
    ]
