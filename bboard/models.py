from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'рубрики'
        verbose_name = 'рубрика'
        ordering = ['name']


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name="товар")
    content = models.TextField(null=True, blank=True, verbose_name="описание")
    price = models.FloatField(null=True, blank=True, verbose_name="цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="опубликовано")
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'объявления'
        verbose_name = 'объявление'
        ordering = ['-published']
