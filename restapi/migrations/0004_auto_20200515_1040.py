# Generated by Django 2.2.5 on 2020-05-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20200515_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='acs',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='aes',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ais',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]