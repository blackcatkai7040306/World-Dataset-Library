# Generated by Django 4.1.7 on 2023-03-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_dataset_thumbnail_alter_dataset_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='slug',
            field=models.SlugField(default='null', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
