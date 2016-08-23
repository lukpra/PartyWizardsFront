from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Drink

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class DrinksView(generic.ListView):
    model = Drink
    context_object_name = 'all_drinks'
    template_name = 'drinks.html'

    def get_queryset(self):
        return Drink.objects.all()

class AddDrinkView(CreateView):
    model = Drink
    fields = ['name', 'recipe', 'picture' ]

'''

def index(request):
    return HttpResponse("Hello, world. You're at the wizards new home.")

'''