# Generated by Django 5.1.5 on 2025-03-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='popular',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
