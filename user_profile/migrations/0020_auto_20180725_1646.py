# Generated by Django 2.0.7 on 2018-07-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0019_auto_20180725_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification',
            field=models.CharField(blank=True, choices=[('1', 'Требуется верификация email и телефона'), ('2', 'Запрошены документы'), ('3', 'Верифицирован'), ('4', 'Отказано'), ('5', 'Ожидает проверки')], max_length=3, null=True, verbose_name='Верифицирован'),
        ),
    ]
