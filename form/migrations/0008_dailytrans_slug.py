# Generated by Django 4.2 on 2024-12-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_remove_dailytrans_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytrans',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
