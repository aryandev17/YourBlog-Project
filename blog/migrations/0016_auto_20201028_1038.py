# Generated by Django 3.1.2 on 2020-10-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20201027_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.URLField(default='/media/hello.jpg'),
        ),
    ]
