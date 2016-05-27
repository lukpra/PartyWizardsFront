from django.views import  generic
from django.shortcuts import render

class IndexView(generic.TemplateView):
   template_name = 'front/index.html'

class ContactView(generic.TemplateView):
   template_name = 'front/contact.html'

class AboutView(generic.TemplateView):
   template_name = 'front/about.html'