# Generated by Django 4.1.2 on 2022-10-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_attribute_2_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_2',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]
