# Generated by Django 2.0.7 on 2018-08-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0011_auto_20180804_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangaward',
            name='is_start',
            field=models.BooleanField(default=False),
        ),
    ]
