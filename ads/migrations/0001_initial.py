# Generated by Django 5.0.7 on 2024-07-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('ad_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
        ),
    ]
