from django.conf.urls import url
from . import views
from django.views.generic import TemplateView



app_name = 'wizzapp'

urlpatterns = [
    # / - index
    url(r'^$', TemplateView.as_view(template_name="wizapp/index.html"), name='index'),
]
