# Generated by Django 5.0.6 on 2024-05-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_mname_sell_manufacturer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='fuel_type',
            new_name='carfuel',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='manufacture_year',
            new_name='carmileage',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='manufacturer_name',
            new_name='carname',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='mileage',
            new_name='carseats',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='number_of_seats',
            new_name='caryear',
        ),
    ]