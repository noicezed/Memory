# Generated by Django 5.0.7 on 2024-07-25 10:17

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_data_joined_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sharelink', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('privacy_settings', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=10)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('link', 'Link')], max_length=5)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('description', models.TextField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='user.album')),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='user.customuser')),
            ],
        ),
    ]
