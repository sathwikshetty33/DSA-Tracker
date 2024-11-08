# Generated by Django 5.1.1 on 2024-10-10 10:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0015_rename_username_teacher_teachername'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='teacherid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rooms',
            name='roomname',
            field=models.CharField(default='class', max_length=20),
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
