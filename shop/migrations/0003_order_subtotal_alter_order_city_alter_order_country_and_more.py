# Generated by Django 4.0.2 on 2022-03-14 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_category_main_image_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='instrument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.instrument'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='newsletter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='telephone',
            field=models.CharField(default='(000)000-0000', max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
