# Generated by Django 4.0.2 on 2022-03-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=255, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Просто текст')),
            ],
        ),
    ]
