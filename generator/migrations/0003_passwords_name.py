# Generated by Django 3.2.2 on 2024-01-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_rename_created_ar_passwords_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwords',
            name='name',
            field=models.CharField(default=22, max_length=14),
            preserve_default=False,
        ),
    ]