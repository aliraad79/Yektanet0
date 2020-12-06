# Generated by Django 3.1.4 on 2020-12-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0007_auto_20201205_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='views',
        ),
        migrations.AddField(
            model_name='click',
            name='advertiser_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='view',
            name='advertiser_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
