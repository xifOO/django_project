# Generated by Django 4.0.3 on 2022-04-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_alter_club_author_alter_club_league_alter_club_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.ImageField(upload_to='./frontend/static/img', verbose_name='logo_club'),
        ),
    ]
