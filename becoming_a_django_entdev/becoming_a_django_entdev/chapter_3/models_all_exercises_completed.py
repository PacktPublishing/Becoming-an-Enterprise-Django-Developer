''' Chapter 3 Models Module '''
from django.contrib.auth.models import (
    AbstractUser,
    #AbstractBaseUser,
)
#from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models.functions import Lower
from djmoney.models.fields import MoneyField
#from djmoney.money import Money
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
    (4, 'Ford'),
    (5, 'GMC'),
    (6, 'Chrysler'),
    (7, 'Dodge'),
    (8, 'Jeep'),
    (9, 'Lincoln'),
    (10, 'Tesla'),
)


class VehicleModel(models.Model):
    '''
    Model Object for Database Table chapter_3_vehicle_model
    '''
    name = models.CharField(
        verbose_name = 'Model',
        max_length = 75,
        unique = True,
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
        '''
        Method to return __str__ format of the VehicleModel Model
        '''
        return str(self.name)

    def natural_key(self):
        '''
        Method to return Natural Key format of the VehicleModel Model
        '''
        return self.__str__()

    class Meta:
        '''
        Meta Sub-Class for chapter_3_vehicle_model Table
        '''
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
    '''
    Model Object for Database Table chapter_3_engine
    '''
    name = models.CharField(
        verbose_name = 'Engine',
        max_length = 75,
        blank = True,
        null = True,
    )
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'model_engine',
        blank = True,
        null = True,
    )

    def __str__(self):
        '''
        Method to return __str__ format of the Engine Model
        '''
        return str(self.name)

    def natural_key(self):
        '''
        Method to return Natural Key format of the Engine Model
        '''
        return self.__str__()

    class Meta:
        '''
        Meta Sub-Class for chapter_3_engine Table
        '''
        ordering = ['name',]
        verbose_name = 'Engine'
        verbose_name_plural = 'Engines'


class engine2(models.Model):
    '''
    Model Object for Database Table chapter_3_practice_engine
    '''
    name = models.CharField(
        verbose_name = 'Engine',
        max_length = 75,
        blank = True,
        null = True,
    )
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'model_engine2',
        blank = True,
        null = True,
    )

    class Meta:
        '''
        Meta Sub-Class for chapter_3_practice_engine Table
        '''
        abstract = True
        db_table = 'chapter_3_practice_engine'
        ordering = ['name',]
        verbose_name = 'Practice Engine'
        verbose_name_plural = 'Practice Engines'


class engine3(engine2):
    '''
    Model Object for Database Table chapter_3_practice_engine
    '''
    other_name = models.CharField(
        verbose_name = 'Other Engine Name',
        max_length = 75,
        blank = True,
        null = True,
    )


class BuickVehicleManager(models.Manager):
    '''
    Model Manager for Buick Only Vehicles
    '''
    def get_queryset(self):
        '''
        Method to return standard/default queryset of the BuickVehicleManager
        '''
        return super().get_queryset().filter(make=1)


class ChevyVehicleManager(models.Manager):
    '''
    Model Manager for Chevy Only Vehicles
    '''
    def get_queryset(self):
        '''
        Method to return standard/default queryset of the ChevyVehicleManager
        '''
        return super().get_queryset().filter(make=3)


class Vehicle(models.Model):
    '''
    Model Object for Database Table chapter_3_vehicle
    '''
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
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete = models.CASCADE,
        verbose_name = 'Model',
        related_name = 'model_vehicle',
        blank = True,
        null = True,
    )
    engine = models.ForeignKey(
        Engine,
        on_delete = models.CASCADE,
        verbose_name = 'Engine',
        related_name = 'engine_vehicle',
        blank = True,
        null = True,
    )

    objects = models.Manager() # The Default Model Manager
    buick_objects = BuickVehicleManager() # The Buick Specific Manager
    chevy_objects = ChevyVehicleManager() # The Chevy Specific Manager

    def __str__(self):
        '''
        Method to return __str__ format of the Vehicle Model
        '''
        MAKE_CHOICES_DICT = dict(MAKE_CHOICES)

        return MAKE_CHOICES_DICT[self.make] + ' ' + self.vehicle_model.name

    def full_vehicle_name(self):
        '''
        Method to return full vehicle name of seller
        '''
        return self.__str__() + ' - ' + self.engine.name

    @property
    def fullname(self):
        '''
        Method to return full name of seller object as a property value
        '''
        return self.__str__() + ' - ' + self.engine.name

    def get_url(self):
        '''
        Method to return relative URL of a seller object edit page
        '''
        from django.urls import reverse
        return reverse('vehicle-detail', kwargs={'id' : self.pk})
        #return reverse('vehicle-detail', kwargs={'vin' : self.vin})

    def get_absolute_url(self, request):
        '''
        Method to return absolute URL of a seller object edit page
        '''
        from django.urls import reverse
        base_url = request.build_absolute_uri('/')[:-1].strip('/')
        return base_url + reverse('vehicle-detail', kwargs={'id' : self.pk})
        #return base_url + reverse('vehicle-detail', kwargs={'vin' : self.vin})

    def natural_key(self):
        '''
        Method to return Natural Key format of the Seller Model
        '''
        return self.full_vehicle_name()

    class Meta:
        '''
        Meta Sub-Class for chapter_3_vehicle Table
        '''
        ordering = ['sold', 'vin',]
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Seller(AbstractUser):
    '''
    Model Object for Database Table chapter_3_seller
    '''
    name = models.CharField(
        verbose_name = 'Business Name',
        max_length = 150,
        blank = True,
        null = True,
    )
    vehicles = models.ManyToManyField(
        Vehicle,
        verbose_name = 'Vehicles',
        related_name = 'vehicle_sellers',
        related_query_name = 'vehicle_seller',
        blank = True,
    )

    def __str__(self):
        '''
        Method to return __str__ format of the Seller Model
        '''
        return str(self.username)

    def natural_key(self):
        '''
        Method to return Natural Key format of the Seller Model
        '''
        return self.__str__()

    class Meta:
        '''
        Meta Sub-Class for chapter_3_seller Table
        '''
        ordering = ['name',]
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

