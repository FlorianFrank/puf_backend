# Generated by Django 4.1.2 on 2023-06-07 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_rename_memory_readlatencytestsmodel_memorylabel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readlatencytestsmodel',
            name='board',
        ),
        migrations.RemoveField(
            model_name='reliabilitytestsmodel',
            name='board',
        ),
        migrations.RemoveField(
            model_name='rowhammeringtestsmodel',
            name='board',
        ),
        migrations.RemoveField(
            model_name='writelatencytestsmodel',
            name='board',
        ),
    ]
