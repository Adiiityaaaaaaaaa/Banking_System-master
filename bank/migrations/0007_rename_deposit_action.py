# Generated by Django 3.2.7 on 2021-09-18 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_transact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deposit',
            new_name='Action',
        ),
    ]
