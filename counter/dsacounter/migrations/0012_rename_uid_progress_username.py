# Generated by Django 5.1.1 on 2024-10-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0011_rename_owner_rooms_teacherid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='uid',
            new_name='username',
        ),
    ]
