from django.db import models


class Position(models.Model):
    name = models.CharField('Название', max_length=30)
    type = models.CharField('Производитель', max_length=40)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товар магазина"