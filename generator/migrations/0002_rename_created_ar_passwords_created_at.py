# Generated by Django 3.2.2 on 2024-01-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwords',
            old_name='created_ar',
            new_name='created_at',
        ),
    ]
