# Generated by Django 4.0.6 on 2022-07-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product_image_alter_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
