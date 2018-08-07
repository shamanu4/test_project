# Generated by Django 2.0.7 on 2018-08-07 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0007_paymenthistory_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockIOWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=200, verbose_name='Кошелёк')),
                ('balance', models.DecimalField(decimal_places=12, max_digits=30)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('end_date', models.DateTimeField(verbose_name='Дата создания')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.PaymentSystem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Кошелёк пользователя',
                'verbose_name_plural': 'Bitcoin кошелёки пользователей',
            },
        ),
    ]
