# Generated by Django 5.0 on 2024-05-16 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='resume_file',
        ),
    ]
