from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Bigser, Gallery, Review, Product, Phones, Emails, Address, SocialLinks, Request


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


class SocialLinksInline(TabularInline):
    model = SocialLinks
    extra = 0


@admin.register(Bigser)
class BigserAdmin(ModelAdmin, TabbedTranslationAdmin):
    fieldsets = [
        ('Меню', {'fields': ['menu_item_main', 'menu_item_about', 'menu_item_products', 'menu_item_partners',
                             'menu_item_reviews'], 'classes': ['collapse']}),
        ('Главный контент', {'fields': ['main_video', 'main_image'], 'classes': ['collapse']}),
        ('О нас',
         {'fields': ['about_title', 'about_text', 'our_mission_title', 'our_mission_text'], 'classes': ['collapse']}),
        ('Продукты', {'fields': ['products_title', 'products_text'], 'classes': ['collapse']}),
        ('Партнеры', {'fields': ['partners_title', 'partners_text'], 'classes': ['collapse']}),
        ('Отзывы', {'fields': ['reviews_title'], 'classes': ['collapse']}),
        ('Заявки', {'fields': ['requests_title', 'requests_text'], 'classes': ['collapse']}),
        ('Контакты', {'fields': ['contacts_title', 'contacts_text', 'map'], 'classes': ['collapse']}),
        ('Футер', {'fields': ['footer_text'], 'classes': ['collapse']}),
    ]
    inlines = [GalleryInline, ReviewInline, PhonesInline, EmailsInline, AddressInline, SocialLinksInline]

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }


@admin.register(Product)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin, PreviewImageMixin):
    fields = ['image_preview', 'image', 'title', 'description']
    readonly_fields = ['image_preview']


@admin.register(Request)
class RequestAdmin(ModelAdmin):
    pass
