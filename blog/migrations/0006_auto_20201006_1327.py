# Generated by Django 3.1.1 on 2020-10-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201006_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_color_code_or_color_name',
            field=models.CharField(default='Example - #0000FF or Blue', max_length=7),
        ),
    ]
