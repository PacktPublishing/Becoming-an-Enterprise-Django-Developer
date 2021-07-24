from datetime                   import datetime
from django.contrib.auth.models import User
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _


class Award(models.Model):
    """
    Awards
    """
    name = models.CharField(
        _('Award Name'),
        max_length = 150,
        unique     = True,
        blank      = True,
        null       = True,
        default    = '',
    )
    earned_date = models.DateField(
        _('Earned On'),
        null      = True,
        blank     = True,
        db_index  = True
    )

    class Meta(object):
        verbose_name        = _('Award')
        verbose_name_plural = _('Awards')

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    Teams
    """
    name = models.CharField(
        _('Island Name'),
        max_length = 150,
        unique     = True,
        blank      = True,
        null       = True,
        default    = '',
    )
    email = models.CharField(
        _('Email'),
        max_length = 256,
        unique     = True,
        blank      = True,
        null       = True,
        default    = '',
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length = 20,
        unique     = True,
        blank      = True,
        null       = True,
        default    = '',
    )
    users = models.ManyToManyField(
        User,
        verbose_name       = _('Assigned Users'),
        blank              = True,
        help_text          = _(
            'List of all the Users assigned to this Team.'
        ),
        related_name       = 'user_team',
        related_query_name = 'user_teams',
    )
    awards = models.ManyToManyField(
        Award,
        verbose_name       = _('Assigned Users'),
        blank              = True,
        help_text          = _(
            'List of all the Users assigned to this Team.'
        ),
        related_name       = 'user_team',
        related_query_name = 'user_teams',
    )

    class Meta(object):
        verbose_name        = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return self.name
