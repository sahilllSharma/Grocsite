# Generated by Django 4.0.2 on 2022-02-21 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fullname',
        ),
        migrations.AddField(
            model_name='client',
            name='phonenumber',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='productdescription',
            field=models.TextField(default='SOMESTRING'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_items', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[(0, 'cancelled Order'), (1, 'placed order'), (2, 'shipped order'), (3, 'delivered order')], max_length=1)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.item')),
            ],
        ),
    ]