# Generated by Django 2.0.5 on 2018-05-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewproducts', '0003_product_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='review',
            name='productid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
