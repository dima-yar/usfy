# Generated by Django 4.2.6 on 2023-11-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_record_record_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_info',
            field=models.CharField(default='Інформація про рекорд відсутня', max_length=1000),
        ),
    ]