# Generated by Django 3.2.7 on 2023-04-25 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_account_name_bank_money_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_money',
            name='transaction_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
