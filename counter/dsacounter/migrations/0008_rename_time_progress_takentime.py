# Generated by Django 5.1.1 on 2024-10-06 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0007_alter_progress_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='time',
            new_name='takentime',
        ),
    ]