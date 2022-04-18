from django.contrib.auth import get_user_model
from django.db import models
from users.models import User


class Stadium(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_stadium'
    )
    name = models.CharField('name_stadium', max_length=255, blank=False, null=False)
    capacity = models.PositiveIntegerField('capacity_stadium', blank=False)

    def __str__(self):
        return f'{self.name}'