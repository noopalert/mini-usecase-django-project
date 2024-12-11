# Generated by Django 4.2 on 2024-12-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTrans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('modes', models.CharField(max_length=100)),
                ('categories', models.CharField(max_length=100)),
                ('subcategories', models.CharField(max_length=100)),
                ('amounts', models.IntegerField()),
                ('types_transaction', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('years', models.IntegerField()),
                ('months', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'dm_dailytrans',
                'managed': False,
            },
        ),
    ]
