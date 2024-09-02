from django.urls import path

from bigser.views import BigserView, CreateRequestView

urlpatterns = [
    path('', BigserView.as_view(), name='index'),
    path('request/', CreateRequestView.as_view(), name='request'),

]