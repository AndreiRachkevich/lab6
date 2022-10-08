from django.db import models


from django.db import models

# встроенная модель пользователя
# нужна для авторов сообщений
from django.contrib.auth.models import User
# тип "временная зона" для получения текущего времени
from django.utils import timezone

class Person(models.Model):
    person_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
class Messages(models.Model):
    chat = models.ForeignKey(
        Person, verbose_name='Чат под человеком',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)



class Mark(models.Model):
    person = models.ForeignKey(Person, verbose_name='Человек', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(
        verbose_name='Оценка')
    pub_date = models.DateTimeField(
        'Дата оценки',
        default=timezone.now)
