# Generated by Django 5.0.7 on 2024-09-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_lastlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='claimable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='withdrawRequest',
            field=models.BooleanField(default=False),
        ),
    ]
