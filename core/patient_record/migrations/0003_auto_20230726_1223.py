# Generated by Django 2.2 on 2023-07-26 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_record', '0002_department_docor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='docor_id',
            new_name='doctor_id',
        ),
    ]
