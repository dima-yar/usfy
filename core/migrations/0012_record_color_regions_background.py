# Generated by Django 4.2.7 on 2023-11-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_record_record_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='color',
            field=models.CharField(choices=[('#5eb1f5', 'record'), ('#8321a3', 'guiness')], default='#5eb1f5', max_length=10),
        ),
        migrations.AddField(
            model_name='regions',
            name='background',
            field=models.ImageField(blank=True, upload_to='upload/bg'),
        ),
    ]
