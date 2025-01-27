# Generated by Django 5.0.6 on 2024-06-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Обучение', 'verbose_name_plural': 'Обучение'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Опыт работы', 'verbose_name_plural': 'Опыт работы'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профиль'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проекты', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Навыки', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='proj ect_images/'),
        ),
    ]
