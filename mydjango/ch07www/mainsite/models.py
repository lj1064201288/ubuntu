from django.db import models

# Create your models here.


class Maker(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pmodel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    nikename = models.CharField(max_length=20, default='超值二手机', verbose_name='摘要')
    description = models.TextField(default='暂无说明', verbose_name='描述')
    price = models.PositiveIntegerField(default=0, verbose_name='价格')
    year = models.PositiveIntegerField(default=2018, verbose_name='年份')
    pmodel = models.ForeignKey(Pmodel, on_delete=models.CASCADE, verbose_name='型号')

    def __str__(self):
        return self.nikename




class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='产品照片')
    url = models.URLField()

    def __str__(self):
        return self.description