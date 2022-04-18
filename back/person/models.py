import re
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from choices import POSITION_CHOICES, NATION_CHOICES
from club.models import Club
from users.models import User


class FootballPerson(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author_person',
        related_name='author_person'
    )
    first_name = models.CharField(max_length=75, blank=False, verbose_name='first_name_person')
    second_name = models.CharField(max_length=75, blank=False, verbose_name='second_name_person')
    position = models.CharField(choices=POSITION_CHOICES, max_length=3, blank=False, verbose_name='position_person')
    nation = models.CharField(choices=NATION_CHOICES, max_length=55, blank=False, verbose_name='nation_person')
    club = models.ForeignKey(
        Club,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='club_person'
    )
    age = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(75),
            MinValueValidator(16),
        ],
        verbose_name='age_person'
    )
    pace = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ],
        verbose_name='pace_person'
    )
    shoots = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ],
        verbose_name='shoots_person'
    )
    passing = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ]
    )
    dribbling = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ],
        verbose_name='dribbling_person'
    )
    defending = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ],
        verbose_name='defending_person'
    )
    physics = models.PositiveSmallIntegerField(
        default=None,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1),
        ],
        verbose_name='physics_person'
    )

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.second_name)

