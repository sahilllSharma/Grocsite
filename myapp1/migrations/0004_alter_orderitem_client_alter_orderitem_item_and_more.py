# Generated by Django 4.0.2 on 2022-02-22 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_remove_client_phonenumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.client'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.item'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('0', 'cancelled order'), ('1', 'placed order'), ('2', 'shipped order'), ('3', 'delivered order')], default='0', max_length=2),
        ),
    ]
