# Generated by Django 4.1.1 on 2022-10-06 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_it_inventory_rename_inventory_design_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design_inventory',
            name='title',
        ),
        migrations.RemoveField(
            model_name='it_inventory',
            name='title',
        ),
    ]
