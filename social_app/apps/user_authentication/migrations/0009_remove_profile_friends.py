# Generated by Django 4.2.6 on 2023-10-10 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0008_profile_friends_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]
