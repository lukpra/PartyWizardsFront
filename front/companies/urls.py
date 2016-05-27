from django.conf.urls import url
from . import views

app_name = 'front'

urlpatterns = [
    #/partywizards/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/partywizards/contact/
    url('^contact/$', views.ContactView.as_view(), name='contact'),

    #/partywizards/about/
    url('^about/$', views.AboutView.as_view(), name='about'),

]