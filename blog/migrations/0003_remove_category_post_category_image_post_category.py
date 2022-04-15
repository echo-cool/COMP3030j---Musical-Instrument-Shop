# Generated by Django 4.0.2 on 2022-04-15 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/blog/image/category'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]