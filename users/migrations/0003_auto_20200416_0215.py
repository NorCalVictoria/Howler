# Generated by Django 3.0.5 on 2020-04-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='clip',
            field=models.FileField(null=True, upload_to='user_video/', verbose_name=''),
        ),
    ]
