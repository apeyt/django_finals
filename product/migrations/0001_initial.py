# Generated by Django 5.1.2 on 2024-10-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('image_src', models.CharField(max_length=255)),
            ],
        ),
    ]
