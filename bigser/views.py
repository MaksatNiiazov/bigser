from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from bigser.models import Bigser, Product, Partners, Review, InstagramLinks, FacebookLinks, WhatsappLinks, Phones, \
    Emails, Address, Request


# Create your views here.

class BigserView(View):

    def get(self, request):
        # return render(request, 'index.html')
        bigser, created = Bigser.objects.get_or_create(
            id=1,
            defaults={
                'menu_item_main': "Главная",
                'menu_item_about': "О нас",
                'menu_item_products_top': "ЛУчшие товары",
                'menu_item_products_new': "Новинки",
                'menu_item_partners': "Партнеры",
                'menu_item_reviews': "Отзывы",
                'main_video': None,
                'main_image': None,
                'about_title': "О нас",
                'about_text': "Bigser Sport — ведущая компания по производству спортивных товаров, базирующаяся в Бишкеке, Кыргызстан. Мы специализируемся на производстве высококачественной спортивной одежды и обуви. Наша миссия — создавать первоклассную продукцию, используя передовые технологии, высококачественное сырье и инновационные дизайны./n Мы работаем на рынке спорта с 1991 года, и Bigser Sport вышла на международный уровень. Мы гордимся тем, что 6 раз снабжали экипировкой участников Олимпийских игр, национальные спортивные команды и чемпионов мира. Мы стремимся не только производить, но и активно участвовать, поддерживать и вносить вклад в многочисленные международные спортивные мероприятия. Наши достижения обусловлены нашей глубокой любовью и страстью к спорту.",
                'our_mission_title': "Наша миссия",
                'our_mission_text': "Наша миссия заключается не только в производстве высококачественной продукции, но и в постоянном развитии и экспериментировании с нашими технологиями. Что касается нашей обуви, она разработана с учетом ортопедических принципов, чтобы обеспечить функциональность, пользу для здоровья и комфорт. Эти принципы применимы не только к нашей обуви, но и к остальной нашей спортивной одежде. Мы верим, что наша работа может вдохновить других на здоровый и активный образ жизни. Кроме того, наша миссия заключается в том, чтобы стать ведущим производителем в Центральной Азии, поощряя таланты и расширяя нашу рабочую силу.",
                'products_title_new': "Новые товары",
                'products_text_new': "Наши товары которые вы можете найти в наших магазинах и заказать",
                'products_title_top': "Лучшие товары",
                'products_text_top': "Наши товары которые вы можете найти в наших магазинах и заказать",
                'partners_title': "Наши партнеры",
                'partners_text': "Мы поддерживаем сотрудничество со множеством компаний",
                'reviews_title': "Наши отзывы",
                'requests_title': "Оставьте заявку",
                'requests_text': "Оставьте заявку и мы свяжемся с вами",
                'contacts_title': "Наши контакты",
                'contacts_text': "Оставьте заявку и мы свяжемся с вами",
                'map': None,
                'email_title': "Электронная почта:",
                'phone_title': "Номер для связи:",
                'address_title': "Адрес нашего офиса:",
                'footer_text': "Bigser Sport — ведущая компания по производству спортивных товаров, базирующаяся в Бишкеке, Кыргызстан.",
                'popup_text': "Ваша заявка успешно отправлена.",
                'popup_button': "Закрыть",
            }
        )
        products_title_top = Product.objects.filter(top=True)
        products_title_new = Product.objects.all().order_by('-new', "-id")
        partners = Partners.objects.all()
        reviews = Review.objects.all()
        phone_main = Phones.objects.filter(main=True).first()
        email_main = Emails.objects.filter(main=True).first()
        address_main = Address.objects.filter(main=True).first()
        instagram_main = InstagramLinks.objects.filter(main=True).first()
        instagram_all = InstagramLinks.objects.all().order_by('main')
        facebook_main = FacebookLinks.objects.filter(main=True).first()
        facebook_all = FacebookLinks.objects.all().order_by('main')
        whatsapp_main = WhatsappLinks.objects.filter(main=True).first()
        whatsapp_all = WhatsappLinks.objects.all().order_by('main')
        message_exist = request.session.pop('message_exist', False)

        meta = {}
        return render(request, 'index.html', {
            'bigser': bigser,
            'top_products': products_title_top,
            'new_products': products_title_new,
            'partners': partners,
            'reviews': reviews,
            'instagram_main': instagram_main,
            'instagram_all': instagram_all,
            'facebook_main': facebook_main,
            'facebook_all': facebook_all,
            'whatsapp_main': whatsapp_main,
            'whatsapp_all': whatsapp_all,
            'phone_main': phone_main,
            'email_main': email_main,
            'address_main': address_main,
            'meta': meta,
            'message_exist': message_exist

        })


class CreateRequestView(View):
    def get(self, request):
        message_exist = request.session.pop('message_exist', False)
        return render(request, 'index.html', {'message_exist': message_exist})

    def post(self, request):
        name = request.POST.get('name', 'Неизвестно')
        phone = request.POST.get('phone', 'Неизвестно')
        email = request.POST.get('email', 'Неизвестно')
        text = request.POST.get('text', 'Неизвестно')
        Request.objects.create(name=name, phone=phone, email=email, message=text)
        messages.success(request, 'Ваша заявка принята')

        request.session['message_exist'] = True
        return redirect('index')
