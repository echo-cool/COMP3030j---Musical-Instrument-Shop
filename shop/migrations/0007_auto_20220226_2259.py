# Generated by Django 2.2.27 on 2022-02-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220226_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='image_url',
        ),
        migrations.AddField(
            model_name='instrument',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/instrument/image/'),
        ),
    ]