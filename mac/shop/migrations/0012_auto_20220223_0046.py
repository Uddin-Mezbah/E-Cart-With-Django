# Generated by Django 3.2.5 on 2022-02-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
