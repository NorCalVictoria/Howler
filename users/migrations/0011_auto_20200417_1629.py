# Generated by Django 3.0.5 on 2020-04-17 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_auto_20200417_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcontent',
            name='post_con',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postcontent',
            name='imagePost',
            field=models.ImageField(default='default.jpg', null=True, upload_to='post_pics'),
        ),
    ]
