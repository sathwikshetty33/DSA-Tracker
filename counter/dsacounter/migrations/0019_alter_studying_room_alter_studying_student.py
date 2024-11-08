# Generated by Django 5.1.1 on 2024-10-10 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0018_alter_rooms_teacherid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='studying',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsacounter.rooms'),
        ),
        migrations.AlterField(
            model_name='studying',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
