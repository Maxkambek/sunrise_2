# Generated by Django 4.1.2 on 2022-10-20 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category_2')),
            ],
        ),
        migrations.CreateModel(
            name='Rate_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_2')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_2')),
            ],
        ),
        migrations.CreateModel(
            name='Attribute_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_2')),
            ],
        ),
    ]
