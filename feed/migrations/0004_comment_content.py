# Generated by Django 4.2.2 on 2023-07-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_post_options_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=0, max_length=3000),
            preserve_default=False,
        ),
    ]
