# Generated by Django 4.1.2 on 2022-10-20 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_attribute_value_alter_attribute_value_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='main.product', verbose_name='продукт'),
        ),
    ]
