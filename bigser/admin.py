from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Bigser, Gallery, Review, Product, Phones, Emails, Address, Request, InstagramLinks, \
    FacebookLinks, WhatsappLinks, Partners


class PreviewImageMixin:

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 200px;">')
        return "-"


class GalleryInline(TabularInline, PreviewImageMixin):
    model = Gallery
    extra = 0
    fields = ['image_preview', 'image']
    readonly_fields = ['image_preview']


class ReviewInline(TabularInline, PreviewImageMixin):
    model = Review
    extra = 0
    fields = ['image_preview', 'image']
    readonly_fields = ['image_preview']


class PhonesInline(TabularInline):
    model = Phones
    extra = 0


class EmailsInline(TabularInline):
    model = Emails
    extra = 0


class AddressInline(TabularInline):
    model = Address
    extra = 0


class PartnersInline(TabularInline):
    model = Partners
    extra = 0


@admin.register(Bigser)
class BigserAdmin(ModelAdmin, TabbedTranslationAdmin):
    fieldsets = [
        ('Logo', {'fields': ['logo', 'only_logo', 'logo_black', 'logo_white'], 'classes': ['collapse']}),
        ('Меню', {'fields': ['menu_item_main', 'menu_item_about', 'menu_item_products_top', 'menu_item_products_new',
                             'menu_item_partners', 'menu_item_reviews', 'menu_item_contacts'],
                  'classes': ['collapse']}),
        ('Главный контент', {'fields': ['main_video', 'main_image'], 'classes': ['collapse']}),
        ('О нас',
         {'fields': ['about_title', 'about_text', 'our_mission_title', 'our_mission_text'], 'classes': ['collapse']}),
        ('Продукты', {'fields': ['products_title_top', 'products_text_top', 'products_title_new', 'products_text_new'],
                      'classes': ['collapse']}),
        ('Партнеры', {'fields': ['partners_title', 'partners_text'], 'classes': ['collapse']}),
        ('Отзывы', {'fields': ['reviews_title'], 'classes': ['collapse']}),
        ('Заявки', {'fields': ['requests_title', 'requests_text'], 'classes': ['collapse']}),
        ('Контакты', {'fields': ['contacts_title', 'contacts_text', 'map'], 'classes': ['collapse']}),
        ('Футер', {'fields': ['footer_text'], 'classes': ['collapse']}),
        ('Попап', {'fields': ['popup_text', 'popup_button'], 'classes': ['collapse']})
    ]
    inlines = [GalleryInline, ReviewInline, PartnersInline, PhonesInline, EmailsInline, AddressInline]

    formfield_overrides = {

    }


@admin.register(Product)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin, PreviewImageMixin):
    fields = ['image_preview', 'image', 'title', 'description', 'new', 'top']
    readonly_fields = ['image_preview']


@admin.register(Request)
class RequestAdmin(ModelAdmin):
    pass


@admin.register(InstagramLinks)
class InstagramLinksAdmin(ModelAdmin):
    pass


@admin.register(FacebookLinks)
class FacebookLinksAdmin(ModelAdmin):
    pass


@admin.register(WhatsappLinks)
class WhatsappLinksAdmin(ModelAdmin):
    pass


@admin.register(Phones)
class PhonesAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


@admin.register(Emails)
class EmailsAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


@admin.register(Address)
class AddressAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass
