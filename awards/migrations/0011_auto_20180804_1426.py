# Generated by Django 2.0.7 on 2018-08-04 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0010_auto_20180804_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rangaward',
            options={'ordering': ('volume',), 'verbose_name': 'Ранговый бонус', 'verbose_name_plural': 'Ранговые бонусы'},
        ),
    ]