# Generated by Django 4.1.2 on 2023-05-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movieUping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('movie_name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('release_year', models.CharField(max_length=20)),
                ('video_id', models.CharField(max_length=20)),
            ],
        ),
    ]