from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название встречи')
    date_meeting = models.DateTimeField(verbose_name='Дата встречи',)
    cost = models.IntegerField(verbose_name='Стоимость посещения')
    description = models.CharField(max_length=255, verbose_name='Описание встречи')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'


class RecordUserMeeting(models.Model):
    user_id = models.PositiveIntegerField(verbose_name='ID пользователя')
    username = models.CharField(verbose_name='Никнейм пользователя', max_length=255)
    full_name = models.CharField(verbose_name='Имя пользователя', max_length=255, blank=True)

    meeting = models.ForeignKey(
        verbose_name='Записавшиеся пользователи',
        to=Meeting,
        related_name='user',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
