# Generated by Django 4.2.6 on 2023-11-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_regions_alter_record_record_holder_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='image',
            field=models.FileField(upload_to='../upload/'),
        ),
    ]
