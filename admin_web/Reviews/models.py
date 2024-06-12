from django.db import models


class Reviews_model(models.Model):
    number = models.IntegerField(verbose_name='Номер отзыва', unique=True)
    rev_Img = models.ImageField(verbose_name='Файл с отзывом', upload_to='images/')

    def __str__(self):
        return f'{self.number} отзыв'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

