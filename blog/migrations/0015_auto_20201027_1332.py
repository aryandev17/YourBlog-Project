# Generated by Django 3.1.2 on 2020-10-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20201027_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.URLField(null=True),
        ),
    ]
