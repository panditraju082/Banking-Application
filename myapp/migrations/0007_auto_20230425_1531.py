# Generated by Django 3.2.7 on 2023-04-25 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_bank_money_transaction_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposie_moeny',
            name='Upi_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upi_money',
            name='Upi_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]