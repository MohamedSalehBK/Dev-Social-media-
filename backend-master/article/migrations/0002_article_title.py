# Generated by Django 3.2 on 2021-04-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.TextField(default='untitled', max_length=500),
        ),
    ]
