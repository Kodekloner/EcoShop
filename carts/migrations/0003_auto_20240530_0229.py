# Generated by Django 3.1 on 2024-05-30 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='is_quantity',
            new_name='is_active',
        ),
    ]
