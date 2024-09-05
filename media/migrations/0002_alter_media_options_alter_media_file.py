# Generated by Django 5.0.7 on 2024-09-03 00:53

import media.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Media Item', 'verbose_name_plural': 'Media Items'},
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to=media.models.get_upload_path),
        ),
    ]
