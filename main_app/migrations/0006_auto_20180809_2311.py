# Generated by Django 2.0.7 on 2018-08-09 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20180808_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripe_user_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]