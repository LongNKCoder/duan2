# Generated by Django 2.2 on 2019-11-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_reportpost_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(choices=[('open', 'Mở'), ('close', 'Đóng')], default='close', max_length=6),
        ),
    ]
