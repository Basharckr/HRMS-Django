# Generated by Django 2.2.2 on 2021-06-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20210609_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='/static/images.profile.png', null=True, upload_to='images'),
        ),
    ]
