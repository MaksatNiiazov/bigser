from modeltranslation.translator import register, TranslationOptions
from .models import Bigser, Product


@register(Bigser)
class BigserTranslationOptions(TranslationOptions):
    fields = ('menu_item_main', 'menu_item_about', 'menu_item_products', 'menu_item_partners', 'menu_item_reviews',
              'about_title', 'about_text',
              'our_mission_title', 'our_mission_text', 'products_title', 'products_text',
              'partners_title', 'partners_text', 'reviews_title', 'requests_title',
              'requests_text', 'contacts_title', 'contacts_text', 'footer_text')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
