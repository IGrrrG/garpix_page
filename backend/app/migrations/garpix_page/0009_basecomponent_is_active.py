# Generated by Django 3.1 on 2022-05-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0008_auto_20220412_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecomponent',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Включено'),
        ),
    ]
