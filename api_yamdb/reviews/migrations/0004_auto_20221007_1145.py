# Generated by Django 2.2.16 on 2022-10-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221007_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий'},
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(),
        ),
    ]
