# Generated by Django 4.2.6 on 2023-11-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_record_record_holder_image_alter_regions_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='record_info',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]