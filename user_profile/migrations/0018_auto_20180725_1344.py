# Generated by Django 2.0.7 on 2018-07-25 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0017_auto_20180724_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-unique_number'], 'permissions': (('is_verified', 'is_verified'), ('can_verify', 'Can verify users')), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
