# Generated by Django 4.0.4 on 2022-04-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_footballperson_age_alter_footballperson_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballperson',
            name='height',
            field=models.IntegerField(default='1', verbose_name='height_person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footballperson',
            name='weight',
            field=models.IntegerField(default='1', verbose_name='weight_person'),
            preserve_default=False,
        ),
    ]
