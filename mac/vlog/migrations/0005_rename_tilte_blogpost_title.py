# Generated by Django 3.2.5 on 2022-02-22 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0004_auto_20220222_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tilte',
            new_name='title',
        ),
    ]
