# Generated by Django 3.0.5 on 2020-04-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200407_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=160, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=160, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
