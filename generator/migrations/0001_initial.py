# Generated by Django 3.2.2 on 2024-01-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=14)),
                ('created_ar', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]