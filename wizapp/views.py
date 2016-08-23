from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Drink

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class DrinkIndexView(generic.ListView):
    model = Drink
    context_object_name = 'all_drinks'
    template_name = 'drink_index.html'

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