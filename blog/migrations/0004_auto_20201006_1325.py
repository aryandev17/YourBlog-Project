# Generated by Django 3.1.1 on 2020-10-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_color_code',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
