# Generated by Django 4.1.2 on 2023-07-02 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_evaluationtask_result_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationtask',
            name='result',
        ),
        migrations.AddField(
            model_name='evaluationtask',
            name='metricsResult',
            field=models.JSONField(default={}),
        ),
    ]
