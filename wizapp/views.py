from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Barcode
from .models import Drink

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class BarcodeView(generic.ListView):
    context_object_name = 'barcodes_all'
    model = Barcode
    template_name = 'barcodes.html'

class BarcodeAdd(CreateView):
    model = Barcode
    fields = ['barcode', 'ingredient']
    success_url = reverse_lazy('wizapp:barcodes')

class DrinkIndexView(generic.ListView):
    model = Drink
    context_object_name = 'all_drinks'
    template_name = 'drinks.html'

    def get_queryset(self):
        return Drink.objects.all()

class AddDrinkView(CreateView):
    model = Drink
    fields = ['name', 'recipe', 'picture' ]

class DrinkDetailView(generic.DetailView):
    model = Drink
    template_name = 'detail.html'

'''

def index(request):
    return HttpResponse("Hello, world. You're at the wizards new home.")

'''