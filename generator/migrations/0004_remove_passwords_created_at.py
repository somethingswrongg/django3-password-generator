# Generated by Django 3.2.2 on 2024-01-13 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_passwords_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwords',
            name='created_at',
        ),
    ]