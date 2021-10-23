from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Award(models.Model):
    '''
    Awards
    '''
    name = models.CharField(
        verbose_name = 'Award Name',
        max_length = 150,
        blank = True,
        null = True,
        default = '',
    )
    earned_date = models.DateField(
        verbose_name = 'Earned On',
        null = True,
        blank = True,
        db_index = True
    )

    class Meta(object):
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.name


class Team(models.Model):
    '''
    Teams
    '''
    name = models.CharField(
        verbose_name = 'Island Name',
        max_length = 150,
        unique = True,
        blank = True,
        null = True,
        default = '',
    )
    email = models.CharField(
        verbose_name = 'Email',
        max_length = 256,
        unique = True,
        blank = True,
        null = True,
        default = '',
    )
    phone_number = models.CharField(
        verbose_name = 'Phone Number',
        max_length = 20,
        unique = True,
        blank = True,
        null = True,
        default = '',
    )
    #users = models.ManyToManyField(
    #    User,
    #    verbose_name = 'Assigned Users',
    #    blank = True,
    #    help_text = 'List of all the Users assigned to this Team.'),
    #    related_name = 'user_team',
    #    related_query_name = 'user_teams',
    #)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name = 'Assigned Users',
        blank = True,
        help_text = 'List of all the Users assigned to this Team.',
        related_name = 'user_team',
        related_query_name = 'user_teams',
    )
    awards = models.ManyToManyField(
        Award,
        verbose_name = 'Assigned Users',
        blank = True,
        help_text = 'List of all the Users assigned to this Team.',
        related_name = 'user_team',
        related_query_name = 'user_teams',
    )

    class Meta(object):
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
