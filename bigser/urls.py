from django.urls import path

from bigser.views import BigserView

urlpatterns = [
    path('', BigserView.as_view(), name='index'),
]