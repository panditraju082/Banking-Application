# Generated by Django 3.2.7 on 2023-04-25 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20230425_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposie_moeny',
            old_name='Upi_time',
            new_name='Deposite_time',
        ),
    ]
