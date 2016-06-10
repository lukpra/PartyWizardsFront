from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



app_name = 'wizapp'

urlpatterns = [
    # / - index
    url(r'^$', views.IndexView.as_view(template_name="index.html"), name='index'),

    #/partywizards/contact/
    url('^add_drink/$', views.AddDrinkView.as_view(), name='add_drink'),

    #/partywizards/about/
    url('^drinks/$', views.DrinksView.as_view(), name='drinks'),
]
