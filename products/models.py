from django.db import models


class Category_2(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='category/',null=True,blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Солнечные панели'
        verbose_name_plural = 'Категория Солнечные панели'


class Product_2(models.Model):
    name = models.CharField(max_length=300, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.PositiveIntegerField(verbose_name='цена')
    brand = models.CharField(max_length=100, verbose_name='марка')
    category = models.ForeignKey(Category_2, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    @property
    def get_rate(self):
        count = self.rate_2_set.count()
        res = 0
        if count == 0:
            return 0
        for i in self.rate_2_set.all():
            res += int(i.rate)
        return res / count

    class Meta:
        verbose_name = 'Солнечные панели'
        verbose_name_plural = 'Солнечные панели'


class ProductImage_2(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='изображение')
    product = models.ForeignKey(Product_2, on_delete=models.CASCADE, related_name='product_2_images')

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображение продукта'


class Attribute_2(models.Model):
    key = models.CharField(max_length=100, verbose_name='ключ')
    value = models.CharField(max_length=120, verbose_name='значение')
    product = models.ForeignKey(Product_2, on_delete=models.CASCADE, verbose_name='продукт',related_name='attribute_product')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Характеристики'
        verbose_name_plural = 'Характеристики'


class Rate_2(models.Model):
    RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    rate = models.IntegerField(choices=RATE, default=2)
    product = models.ForeignKey(Product_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
