# Generated by Django 4.1.7 on 2023-03-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_dataset_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='file',
            field=models.FileField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
