# Generated by Django 3.0.2 on 2020-04-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auto_20200331_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
