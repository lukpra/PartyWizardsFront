from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



app_name = 'wizapp'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(template_name="index.html"), name="index"),

    url(r'^drinks/$', views.DrinksView.as_view(), name="drinks"),

    url(r'^drinks/add/$', views.AddDrinkView.as_view(), name="drink-add")
]
