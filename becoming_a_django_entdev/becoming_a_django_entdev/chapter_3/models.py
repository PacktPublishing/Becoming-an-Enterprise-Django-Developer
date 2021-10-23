from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models.functions import Lower
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


YESNO_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)

MAKE_CHOICES = (
    (0, '------'),
    (1, 'Buick'),
    (2, 'Cadillac'),
    (3, 'Chevrolet'),
    (4, 'GMC'),
    (5, 'Chrysler'),
    (6, 'Dodge'),
    (7, 'Jeep'),
    (8, 'RAM'),
    (9, 'Ford'),
    (10, 'Lincoln'),
)


class Vehicle_Model(models.Model):
    name = models.CharField(
        verbose_name = 'Model',
        max_length = 75,
        blank = True,
        null = True,
    )
    make = models.PositiveIntegerField(
        choices = MAKE_CHOICES,
        verbose_name = 'Make/Manufacturer',
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['name',]
        verbose_name = 'Vehicle Model'
        verbose_name_plural = 'Vehicle Models'
        indexes = [
            models.Index(fields=['name']),
            #models.Index(fields=['name', 'make']),
            models.Index(fields=['-name'], name='desc_name_idx'),
            models.Index(Lower('name').desc(), name='lower_name_idx')
        ]


class Engine(models.Model):
    name = models.CharField(
        verbose_name = 'Engine',
        max_length = 75,
        blank = True,
        null = True,
    )
    model = models.ForeignKey(
        Vehicle_Model,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'engine_model',
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['name',]
        verbose_name = 'Engine'
        verbose_name_plural = 'Engines'


class engine2(models.Model):
    name = models.CharField(
        verbose_name = 'Engine',
        max_length = 75,
        blank = True,
        null = True,
    )
    model = models.ForeignKey(
        Vehicle_Model,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'engine2_model',
        blank = True,
        null = True,
    )

    class Meta(object):
        abstract = True
        db_table = 'chapter_3_practice_engine'
        ordering = ['name',]
        verbose_name = 'Practice Engine'
        verbose_name_plural = 'Practice Engines'


class engine3(engine2):
    other_name = models.CharField(
        verbose_name = 'Other Engine Name',
        max_length = 75,
        blank = True,
        null = True,
    )


class BuickVehicleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(make=1)


class ChevyVehicleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(make=3)


class Vehicle(models.Model):
    vin = models.CharField(
        verbose_name = 'VIN',
        max_length = 17,
        unique = True,
        blank = True,
        null = True,
    )
    sold = models.BooleanField(
        verbose_name = 'Sold?',
        choices = YESNO_CHOICES,
        default = False,
        blank = True,
        null = True,
    )
    price = MoneyField(
        max_digits = 19,
        decimal_places = 2,
        default_currency = 'USD',
        null = True,
        validators = [
            #MinMoneyValidator(400),
            #MaxMoneyValidator(400000),
            #MinMoneyValidator(Money(500, 'EUR')),
            #MaxMoneyValidator(Money(500000, 'EUR')),
            MinMoneyValidator({'EUR': 500, 'USD': 400}),
            MaxMoneyValidator({'EUR': 500000, 'USD': 400000}),
        ]
    )
    make = models.PositiveIntegerField(
        choices = MAKE_CHOICES,
        verbose_name = 'Vehicle Make/Brand',
        blank = True,
        null = True,
    )
    model = models.ForeignKey(
        Vehicle_Model,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'vehicle_model',
        blank = True,
        null = True,
    )
    engine = models.ForeignKey(
        Engine,
        on_delete = models.CASCADE,
        verbose_name = 'Engine',
        related_name = 'engine',
        blank = True,
        null = True,
    )

    objects = models.Manager() # The Default Model Manager
    buick_objects = BuickVehicleManager() # The Buick Specific Manager
    chevy_objects = ChevyVehicleManager() # The Chevy Specific Manager

    def __str__(self):
        MAKE_CHOICES_DICT = dict(MAKE_CHOICES)

        return MAKE_CHOICES_DICT[self.make] + ' ' + self.model.name

    def full_vehicle_name(self):
        return self.__str__() + ' - ' + self.engine.name

    @property
    def fullname(self):
        return self.__str__() + ' - ' + self.engine.name

    def get_url(self):
        from django.urls import reverse
        return reverse('vehicle-detail', kwargs={'id' : self.pk})
        #return reverse('vehicle-detail', kwargs={'vin' : self.vin})

    def get_absolute_url(self, request):
        from django.urls import reverse
        base_url = request.build_absolute_uri('/')[:-1].strip('/')
        return base_url + reverse('vehicle-detail', kwargs={'id' : self.pk})
        #return base_url + reverse('vehicle-detail', kwargs={'vin' : self.vin})

    class Meta(object):
        ordering = ['sold', 'vin',]
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Seller(AbstractUser):
    name = models.CharField(
        verbose_name = 'Seller Name',
        max_length = 150,
        blank = True,
        null = True,
    )
    vehicles = models.ManyToManyField(
        Vehicle,
        verbose_name = 'Vehicles',
        related_name = 'vehicles',
        related_query_name = 'vehicle',
        blank = True,
    )

    def __str__(self):
        return self.username

    class Meta(object):
        ordering = ['name',]
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
