# Generated by Django 4.1.2 on 2022-10-20 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': 'Характеристики', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория Орготехника', 'verbose_name_plural': 'Категория Орготехника'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Орготехника', 'verbose_name_plural': 'Орготехники'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Изображение продукта', 'verbose_name_plural': 'Изображение продукта'},
        ),
        migrations.AddField(
            model_name='attribute',
            name='key_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='ключ'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='key_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='ключ'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='value_ru',
            field=models.CharField(max_length=120, null=True, verbose_name='value'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='value_uz',
            field=models.CharField(max_length=120, null=True, verbose_name='value'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='key',
            field=models.CharField(max_length=100, verbose_name='ключ'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.CharField(max_length=120, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='марка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='продукт'),
        ),
    ]