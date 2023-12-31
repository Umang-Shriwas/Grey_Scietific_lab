# Generated by Django 2.2 on 2023-07-26 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230722_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('diagnostics', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Department'),
        ),
    ]
