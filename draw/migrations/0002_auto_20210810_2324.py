# Generated by Django 3.2.6 on 2021-08-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0001_squashed_0006_listing_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='street_address',
            field=models.CharField(max_length=50),
        ),
    ]
