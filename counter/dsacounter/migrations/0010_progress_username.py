# Generated by Django 5.1.1 on 2024-10-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0009_rooms_teacher_remove_progress_username_progress_uid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]