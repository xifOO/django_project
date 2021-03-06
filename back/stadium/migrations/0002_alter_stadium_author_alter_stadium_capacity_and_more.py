# Generated by Django 4.0.3 on 2022-04-15 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stadium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_stadium', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stadium',
            name='capacity',
            field=models.PositiveIntegerField(verbose_name='capacity_stadium'),
        ),
        migrations.AlterField(
            model_name='stadium',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name_stadium'),
        ),
    ]
