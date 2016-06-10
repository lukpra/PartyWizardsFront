from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from . import views



app_name = 'wizapp'

urlpatterns = [
    # / - index
    url(r'^$', views.IndexView.as_view(template_name="index.html"), name='index'),

    # add_drink/
    url('^add_drink/$', views.AddDrinkView.as_view(), name='add_drink'),

    # /drinks/
    url('^drinks/$', views.DrinksView.as_view(), name='drinks'),

    # /barcode
    url(r'^barcode/$', views.BarcodeView.as_view(),name="barcodes"),

    # /barcode/add/
    url(r'^barcode/add/$', views.BarcodeAdd.as_view(),name="barcode-add")
]
