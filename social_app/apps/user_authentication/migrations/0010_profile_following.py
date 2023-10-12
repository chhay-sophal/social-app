# Generated by Django 4.2.6 on 2023-10-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0009_remove_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='user_authentication.profile'),
        ),
    ]