# Generated by Django 2.2.5 on 2019-10-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0006_auto_20191022_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='pic/default.jpg', upload_to='pic'),
        ),
    ]
