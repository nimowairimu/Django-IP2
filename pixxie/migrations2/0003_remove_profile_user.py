# Generated by Django 3.1.7 on 2021-03-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixxie', '0002_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
