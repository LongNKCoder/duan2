# Generated by Django 2.2 on 2019-10-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_reportpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pic',
            field=models.ImageField(default='post/category/default.jpg', upload_to='post/category'),
        ),
    ]