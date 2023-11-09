# Generated by Django 4.2.2 on 2023-06-29 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_alter_friendrequest_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_friend_requests', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='friendrequest',
            unique_together={('from_user', 'to_user', 'is_accepted')},
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='users',
        ),
    ]