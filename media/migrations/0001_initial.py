# Generated by Django 5.0.7 on 2024-09-02 23:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('link', 'Link')], max_length=5)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('description', models.TextField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='album.album')),
            ],
        ),
    ]
