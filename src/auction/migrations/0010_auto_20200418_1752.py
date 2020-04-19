# Generated by Django 3.0.2 on 2020-04-18 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auctionitem_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], default='Used', max_length=10),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]