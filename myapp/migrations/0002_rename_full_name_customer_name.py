# Generated by Django 3.2.7 on 2023-04-21 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Full_name',
            new_name='Name',
        ),
    ]
