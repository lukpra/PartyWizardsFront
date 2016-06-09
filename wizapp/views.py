from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.TemplateView):
    template_name = 'index.html'

'''

def index(request):
    return HttpResponse("Hello, world. You're at the wizards new home.")

'''