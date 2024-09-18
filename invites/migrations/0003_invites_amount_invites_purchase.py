# Generated by Django 5.0.7 on 2024-09-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0002_alter_invites_fromuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='invites',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invites',
            name='purchase',
            field=models.BooleanField(default=False),
        ),
    ]
