# Generated by Django 4.2 on 2023-04-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_options_menu_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='branch',
            field=models.IntegerField(default=0, verbose_name='Ветка меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.SlugField(),
        ),
    ]