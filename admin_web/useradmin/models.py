from django.db import models


class Recruitment_course(models.Model):
    flag = models.BooleanField(verbose_name='Набор', default=False)

    def __str__(self):
        if self.flag:
            return 'Набор идёт'
        return 'Набора сейчас нет'

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Набор'


class Users(models.Model):
    user_id = models.IntegerField(verbose_name='ID пользователя', unique=True)
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True)
    testing_attempts = models.IntegerField(verbose_name='Количесво попыток в тесте', default=1, blank=True)
    user_lvl = models.IntegerField(verbose_name='Уровень пользователя', default=1, blank=True)
    subscription_day = models.PositiveIntegerField(verbose_name='Дней подписки', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата, когда первый раз зашел', auto_now_add=True)
    access_quiz = models.BooleanField(verbose_name='Доступ к тесту')
    subscription_name = models.CharField(verbose_name='Название подписки', blank=True, max_length=255)
    email_google = models.EmailField(verbose_name='Email в Google', blank=True)
    referal = models.IntegerField('Id пользователя по чьей ссылке  перешел', blank=True, null=True)
    referal_sub = models.BooleanField(verbose_name='Подписка за реферальную систему', default=False)

    def __str__(self):
        return f'@{self.user_name} {self.user_id}' if self.user_name is not None else f'{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Chats(models.Model):
    title = models.CharField(verbose_name='Название чата', max_length=255)
    tg_id = models.BigIntegerField(verbose_name='ID в Telegram', unique=True)

    def __str__(self):
        return f'{self.tg_id} {self.title}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Channels(models.Model):
    title = models.CharField(verbose_name='Название канала', max_length=255)
    tg_id = models.BigIntegerField(verbose_name='ID в Telegram', unique=True)

    def __str__(self):
        return f'{self.tg_id} {self.title}'

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


# class Statistics(models.Model):
#     date= models.DateField(verbose_name='День', auto_now_add=True)
#     new_user = models.PositiveIntegerField('Количество новых пользователей', default=0)
#     purchase_month = models.PositiveIntegerField('Количество пользователей, купивших подписку на месяц', default=0)
#     purchase_three_month = models.PositiveIntegerField('Количество пользователей, купивших подписку на 3 месяца', default=0)
#     purchase_meeting = models.PositiveIntegerField('Количество пользователей, оплативших собрание', default=0)
#     passed_test = models.PositiveIntegerField('Количество пользователей, прошедших тест', default=0)
#     failed_test = models.PositiveIntegerField('Количество пользователей, не сдавших тест', default=0)
#
#     class Meta:
#         verbose_name = 'Статистика'
#         verbose_name_plural = 'Статистика'
