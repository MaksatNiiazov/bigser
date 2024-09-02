# Generated by Django 5.1 on 2024-09-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigser', '0007_address_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigser',
            name='popup_text',
            field=models.TextField(blank=True, null=True, verbose_name='попап Текст'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='попап Текст'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_text_ky',
            field=models.TextField(blank=True, null=True, verbose_name='попап Текст'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='попап Текст'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='попап Заголовок'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='попап Заголовок'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_title_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='попап Заголовок'),
        ),
        migrations.AddField(
            model_name='bigser',
            name='popup_title_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='попап Заголовок'),
        ),
    ]
