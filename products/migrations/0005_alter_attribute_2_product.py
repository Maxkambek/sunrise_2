# Generated by Django 4.1.2 on 2022-10-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_attribute_2_options_alter_attribute_2_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute_2',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_product', to='products.product_2', verbose_name='продукт'),
        ),
    ]
