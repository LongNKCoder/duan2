# Generated by Django 2.2 on 2019-12-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0007_auto_20191026_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
