# Generated by Django 4.2.3 on 2023-07-21 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]