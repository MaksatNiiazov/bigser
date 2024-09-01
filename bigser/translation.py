from modeltranslation.translator import register, TranslationOptions
from .models import Bigser, Product, Phones, Emails, Address


@register(Bigser)
class BigserTranslationOptions(TranslationOptions):
    fields = ('menu_item_main', 'menu_item_about', 'menu_item_products_new', 'menu_item_products_top',
              'menu_item_partners', 'menu_item_reviews', 'menu_item_contacts',
              'about_title', 'about_text',
              'our_mission_title', 'our_mission_text', 'products_title_top', 'products_text_top', 'products_title_new', 'products_text_new',
              'partners_title', 'partners_text', 'reviews_title', 'requests_title',
              'requests_text', 'contacts_title', 'contacts_text', 'footer_text')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Phones)
class PhonesTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Emails)
class EmailsTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('name',)


