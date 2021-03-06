# Generated by Django 2.2 on 2022-03-31 06:45

import coplate.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0003_auto_20220319_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('restaurant_name', models.CharField(max_length=20)),
                ('restaurant_link', models.URLField(verbose_name=coplate.validators.validate_restaurant_link)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('image1', models.ImageField(upload_to='review_pics')),
                ('image2', models.ImageField(blank=True, upload_to='review_pics')),
                ('image3', models.ImageField(blank=True, upload_to='review_pics')),
                ('content', models.TextField()),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
