# Generated by Django 4.0.2 on 2022-04-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_rename_no_of_items_orderitem_items_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
