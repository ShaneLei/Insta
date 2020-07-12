# Generated by Django 3.0.8 on 2020-07-11 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
