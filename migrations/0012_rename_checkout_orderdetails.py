# Generated by Django 4.1.6 on 2023-03-09 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_checkout_pincode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Checkout',
            new_name='orderdetails',
        ),
    ]