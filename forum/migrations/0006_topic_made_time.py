# Generated by Django 2.0.7 on 2018-12-09 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='made_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
