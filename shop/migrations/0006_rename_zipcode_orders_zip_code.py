# Generated by Django 4.1.4 on 2023-07-29 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='zipcode',
            new_name='zip_code',
        ),
    ]