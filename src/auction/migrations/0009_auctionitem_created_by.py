# Generated by Django 3.0.2 on 2020-04-06 21:45

import crum
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0008_auto_20200404_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='created_by',
            field=models.ForeignKey(default=crum.get_current_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
