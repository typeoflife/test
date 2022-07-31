import pytz
from django.core.validators import RegexValidator
from django.db import models

PHONE_COMPANY = (
    ('mts', 'МТС'),
    ('megafon', 'Мегафон'),
    ('rosstelecom', 'Росстелеком'),
    ('beeline', 'Билайн'),
    ('tele2', 'Теле2'),
    ('yota', 'Йота'),
)

# TIMEZONES = (
#     ('UTC−12:00', 'UTC−12:00'),
#     ('UTC−11:00', 'UTC−11:00'),
#     ('UTC−10:00', 'UTC−10:00'),
#     ('UTC−9:30', 'UTC−9:30'),
#     ('UTC−9:00', 'UTC−9:00'),
#     ('UTC−8:00', 'UTC−8:00'),
#     ('UTC−7:00', 'UTC−7:00'),
#     ('UTC−6:00', 'UTC−6:00'),
#     ('UTC−5:00', 'UTC−5:00'),
#     ('UTC−4:00', 'UTC−4:00'),
#     ('UTC−3:30', 'UTC−3:30'),
#     ('UTC−3:00', 'UTC−3:00'),
#     ('UTC−2:00', 'UTC−2:00'),
#     ('UTC−1:00', 'UTC−1:00'),
#     ('UTC−0:00', 'UTC−0:00'),
#     ('UTC+1:00', 'UTC+1:00'),
#     ('UTC+2:00', 'UTC+2:00'),
#     ('UTC+2:00', 'UTC+2:00'),
#     ('UTC+3:30', 'UTC+3:30'),
#     ('UTC+4:00', 'UTC+4:00'),
#     ('UTC+4:30', 'UTC+4:30'),
#     ('UTC+5:00', 'UTC+5:00'),
#     ('UTC+5:30', 'UTC+5:30'),
#     ('UTC+5:45', 'UTC+5:45'),
#     ('UTC+6:00', 'UTC+6:00'),
#     ('UTC+6:30', 'UTC+6:30'),
#     ('UTC+7:00', 'UTC+7:00'),
#     ('UTC+8:00', 'UTC+8:00'),
#     ('UTC+8:45', 'UTC+8:45'),
#     ('UTC+9:00', 'UTC+9:00'),
#     ('UTC+9:30', 'UTC+9:30'),
#     ('UTC+10:00', 'UTC+10:00'),
#     ('UTC+10:30', 'UTC+10:30'),
#     ('UTC+11:00', 'UTC+11:00'),
#     ('UTC+12:00', 'UTC+12:00'),
#     ('UTC+12:45', 'UTC+12:45'),
#     ('UTC+13:00', 'UTC+13:00'),
#     ('UTC+14:00', 'UTC+14:00'),
# )

STATUS = (
    ('begin', 'В процессе'),
    ('done', 'Завершено'),

)


class Newsletter(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(verbose_name='Текст сообщения')
    filter = models.CharField(verbose_name='Фильтр', max_length=20)
    end_time = models.DateTimeField()

    def __str__(self):
        return f'Рассылка с номером {self.id}, текст: {self.message}, отфильтровали по: {self.filter}'

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_number = models.IntegerField(verbose_name='Номер телефона',
                                       validators=[RegexValidator(r'^\d{11}$',
                                                                  'Number must be 11 digits', 'Invalid number')])
    operator = models.CharField(verbose_name='Мобильный оператор', choices=PHONE_COMPANY, max_length=11)
    tag = models.CharField(verbose_name='Произвольная метка', max_length=30)
    timezone = models.CharField(verbose_name='Часовой пояс', choices=TIMEZONES, max_length=32)

    def __str__(self):
        return f'Номер клиента {self.id} с телефоном: {self.phone_number} и оператором: {self.operator}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name='Статус отправки', choices=STATUS, max_length=10, default='begin')
    newsletter_id = models.ForeignKey(Newsletter, verbose_name='ID рассылки',
                                      related_name='messages', on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, verbose_name='ID клиента',
                                  related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f'Номер сообщения {self.id}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
