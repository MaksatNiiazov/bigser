from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Bigser(models.Model):
    logo = models.FileField(blank=True, null=True, verbose_name=_('Логотип'))
    only_logo = models.FileField(default=False, null=True, verbose_name=_('Логотип только'))
    logo_black = models.FileField(default=False, null=True, verbose_name=_('Логотип черный'))
    logo_white = models.FileField(default=False, null=True, verbose_name=_('Логотип белый'))

    # menu
    menu_item_main = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('меню Главное'))
    menu_item_about = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('меню О нас'))
    menu_item_products_top = models.CharField(max_length=100, blank=True, null=True,
                                              verbose_name=_('меню Продукты бестселлеры'))
    menu_item_products_new = models.CharField(max_length=100, blank=True, null=True,
                                              verbose_name=_('меню Продукты новинки'))
    menu_item_partners = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('меню Партнеры'))
    menu_item_reviews = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('меню Отзывы'))
    menu_item_contacts = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('меню Контакты'))

    # content

    main_video = models.FileField(blank=True, null=True, verbose_name=_('Видео'))
    main_image = models.FileField(blank=True, null=True, verbose_name=_('Картинка'))

    # about

    about_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('о нас Заголовок'))
    about_text = models.TextField(blank=True, null=True, verbose_name=_('о нас Текст'))

    our_mission_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('наша миссия Заголовок'))
    our_mission_text = models.TextField(blank=True, null=True, verbose_name=_('наша миссия Текст'))

    # products

    products_title_top = models.CharField(max_length=100, blank=True, null=True,
                                          verbose_name=_('продукты Заголовок бестселлеры'))
    products_text_top = models.TextField(blank=True, null=True, verbose_name=_('продукты Текст бестселлеры'))

    products_title_new = models.CharField(max_length=100, blank=True, null=True,
                                          verbose_name=_('продукты Заголовок новинки'))
    products_text_new = models.TextField(blank=True, null=True, verbose_name=_('продукты Текст новинки'))

    # partners

    partners_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('партнеры Заголовок'))
    partners_text = models.TextField(blank=True, null=True, verbose_name=_('партнеры Текст'))

    # reviews

    reviews_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('отзывы Заголовок'))

    # requests
    requests_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('заявки Заголовок'))
    requests_text = models.TextField(blank=True, null=True, verbose_name=_('заявки Текст'))

    # contacts
    contacts_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('контакты Заголовок'))
    contacts_text = models.TextField(blank=True, null=True, verbose_name=_('контакты Текст'))

    map = models.TextField(blank=True, null=True, verbose_name=_('контакты Карта'))
    email_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('контакты Email'))
    phone_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('контакты Телефон'))
    address_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('контакты Адрес'))

    #

    footer_text = models.TextField(blank=True, null=True, verbose_name=_('контакты Текст'))

    def __str__(self):
        return 'Контент сайта'

    def save(self, *args, **kwargs):
        if not self.pk and Bigser.objects.exists():
            raise Exception('Невозможно создать более одного экземпляра модели Bigser.')
        return super(Bigser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Контент сайта')
        verbose_name_plural = _('Контент сайта')


class Product(models.Model):
    image = models.FileField(blank=True, null=True, verbose_name=_('продукт Изображение'))
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('продукт Заголовок'))
    description = models.TextField(blank=True, null=True, verbose_name=_('продукт Описание'))
    new = models.BooleanField(default=False)
    top = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')


class Gallery(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, verbose_name=_('галерея Страница'),
                             related_name='gallery')
    image = models.FileField(blank=True, null=True, verbose_name=_('галерея Изображение'))
    text = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('галерея Текст'))

    class Meta:
        verbose_name = _('изоражение галереи')
        verbose_name_plural = _('изображения галереи')


class Partners(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, verbose_name=_('Партнер'), related_name='partners')
    logo = models.FileField(blank=True, null=True, verbose_name=_('Партнер Логотип'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Партнер Название'))

    class Meta:
        verbose_name = _('партнер')
        verbose_name_plural = _('партнеры')


class Review(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, verbose_name=_('отзыв Страница'), related_name='review')
    image = models.FileField(blank=True, null=True, verbose_name=_('отзыв Изображение'))

    class Meta:
        verbose_name = _('отзыв')
        verbose_name_plural = _('отзывы')


class Phones(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, related_name='phones',
                             verbose_name=_('телефон Страница'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Название'))
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Телефон'))

    class Meta:
        verbose_name = _('телефон')
        verbose_name_plural = _('телефоны')


class Emails(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, related_name='emails', verbose_name=_('email Страница'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Название'))
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Email'))

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')


class Address(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, related_name='address_set',
                             verbose_name=_('адрес Страница'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Название'))
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Адрес'))

    class Meta:
        verbose_name = _('адрес')
        verbose_name_plural = _('адреса')


class InstagramLinks(models.Model):
    main = models.BooleanField(default=False, verbose_name=_('Главная'))
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Ссылка'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Название'))


class SocialLinks(models.Model):
    page = models.ForeignKey(Bigser, on_delete=models.CASCADE, verbose_name=_('социальная Страница'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Название'))
    icon = models.FileField(blank=True, null=True, verbose_name=_('Иконка'))
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Ссылка'))

    class Meta:
        verbose_name = _('социальная сеть')
        verbose_name_plural = _('социальные сети')


class Request(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Имя'))
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Email'))
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Телефон'))
    message = models.TextField(blank=True, null=True, verbose_name=_('Сообщение'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Создано'))

    class Meta:
        verbose_name = _('заявка')
        verbose_name_plural = _('заявки')
