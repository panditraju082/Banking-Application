# Generated by Django 3.2.7 on 2023-04-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230424_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank_money',
            old_name='Account_name',
            new_name='Account_number',
        ),
    ]
