# Generated by Django 4.2.7 on 2023-11-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_record_color_regions_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_holders_age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
