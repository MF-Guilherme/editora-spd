# Generated by Django 5.0.3 on 2024-07-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.IntegerField(),
        ),
    ]
