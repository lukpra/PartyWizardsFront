from django.conf.urls import url
from . import views
from django.views.generic import TemplateView



app_name = 'wizapp'

urlpatterns = [
    # / - index
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

    # /barcode/add/
    url(r'^barcode/$', views.BarcodeView.as_view(),name="barcodes")
]
