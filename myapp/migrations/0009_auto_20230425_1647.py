# Generated by Django 3.2.7 on 2023-04-25 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_upi_time_deposie_moeny_deposite_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposie_moeny',
            old_name='Deposite_time',
            new_name='transaction_time',
        ),
        migrations.RenameField(
            model_name='upi_money',
            old_name='Upi_time',
            new_name='transaction_time',
        ),
    ]
