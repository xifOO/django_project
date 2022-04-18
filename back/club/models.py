from django.contrib.auth import get_user_model
from django.db import models
from choices import LEAGUE_CHOICES
from stadium.models import Stadium
from users.models import User


class Club(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_club'
    )
    name = models.CharField(max_length=155, blank=False, null=False, verbose_name='name_club')
    league = models.CharField(choices=LEAGUE_CHOICES, max_length=155, verbose_name='league_club')
    logo = models.ImageField(upload_to='./frontend/static/img', verbose_name='logo_club')
    stadium = models.OneToOneField(
        Stadium,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='stadium_club',
    )

    def __str__(self):
        return f'{self.name}'


