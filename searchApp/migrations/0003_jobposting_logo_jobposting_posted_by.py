# Generated by Django 5.0 on 2024-05-17 18:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_remove_jobposting_last_updated_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='logo',
            field=models.ImageField(null=True, upload_to='company_logo/'),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
