# Generated by Django 4.1.2 on 2023-07-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_detection', '0003_remove_ttydevicemodel_node_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttydevicemodel',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
