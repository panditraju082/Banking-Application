# Generated by Django 3.2.7 on 2023-04-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_customer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Balance',
            field=models.CharField(default='600', max_length=90),
        ),
    ]