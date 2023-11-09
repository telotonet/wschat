# Generated by Django 4.2.2 on 2023-07-31 07:53

import django.core.validators
from django.db import migrations, models
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='post_photos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.ManyToManyField(blank=True, to='feed.photo', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), feed.models.validate_max_files]),
        ),
    ]
