# Generated by Django 5.2.3 on 2025-07-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
