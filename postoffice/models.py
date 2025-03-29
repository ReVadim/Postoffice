from django.db import models
from django.core.validators import MinValueValidator


class BasePostData(models.Model):
    """ Base model of information about parcels and letters """

    sender = models.CharField(max_length=255, verbose_name='отправитель')
    recipient = models.CharField(max_length=255, verbose_name='получатель')
    dispatch_point = models.CharField(max_length=300, verbose_name='пункт отправки')
    receive_point = models.CharField(max_length=300, verbose_name='пункт получения')
    dispatch_postal_code = models.PositiveIntegerField(verbose_name='индекс места отправки')
    receive_postal_code = models.PositiveIntegerField(verbose_name='индекс места получения')

    class Meta:
        abstract = True
    

class Letters(BasePostData, models.Model):
    """ Letters """

    LETTER_TYPES = [
        (10, 'regular'),
        (20, 'registered'),
        (30, 'valuable'),
        (40, 'express'),
    ]

    letter_type = models.PositiveIntegerField(verbose_name='тип письма', choices=LETTER_TYPES)
    letter_weight = models.DecimalField(
        verbose_name='вес письма', help_text='0.00', max_digits=5, decimal_places=2, validators=[MinValueValidator(0)]
        )
    
    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
        db_table = 'letters'
        ordering = ['dispatch_point']

    def __str__(self):
        return f'Sender: {self.sender} | Letter: {self.letter_type}'

    
class Parcels(BasePostData, models.Model):
    """ Parcels """

    PARSEL_TYPES = [
        (50, 'small'),
        (51, 'package'),
        (60, '1st_class'),
        (61, 'valuable'),
        (70, 'international'),
        (71, 'express'),
    ]
    phone_number = models.CharField(max_length=50, verbose_name='телефон для извещения')
    parcel_type = models.PositiveBigIntegerField(verbose_name='тип посылки', choices=PARSEL_TYPES)
    payment_amount = models.DecimalField(
        verbose_name='сумма платежа', help_text='0.00', max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
        )
    
    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
        db_table = 'parcels'
        ordering = ['dispatch_point']

    def __str__(self):
        return f'Sender: {self.sender} | Parcel: {self.parcel_type}'
