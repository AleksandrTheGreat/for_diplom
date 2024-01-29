from django.db import models

class Price(models.Model):
    title = models.CharField('Название', max_length=100)
    cena = models.CharField('Цена',max_length=100)
    image = models.CharField('Картинка', max_length=100)

    def __str__(self):
        return self.title
    pass

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Contacts(models.Model):
    mail = models.EmailField(verbose_name='Эл.Почта')
    workphone = models.CharField(verbose_name='Раб.Телефон', max_length=20)
    mobilephone = models.CharField(verbose_name='Сот.Телефон', max_length=20)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
