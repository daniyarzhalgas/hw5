# Generated by Django 5.1.6 on 2025-02-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
