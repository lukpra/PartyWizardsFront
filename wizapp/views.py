from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Barcode

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class BarcodeView(generic.ListView):
    context_object_name = 'barcodes_all'
    model = Barcode
    template_name = 'barcodes.html'

class AlcoholCreate(CreateView):
    model = Barcode
    fields = ['name', 'type', 'is_tasty']
'''

def index(request):
    return HttpResponse("Hello, world. You're at the wizards new home.")

'''