from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



app_name = 'wizapp'

urlpatterns = [
    # / - index
    url(r'^$', views.IndexView.as_view(template_name="index.html"), name='index'),

    #/partywizards/contact/

    url(r'^drinks/$', views.DrinkIndexView.as_view(), name="drinks"),

    url(r'^(?P<pk>[0-9]+)/$', views.DrinkDetailView.as_view(), name='detail'),

    url(r'^drinks/add/$', views.AddDrinkView.as_view(), name="drink-add")
]
