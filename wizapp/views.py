from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Drink

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class AddDrinkView(CreateView):
    model = Drink
    fields = ['name', 'recipe', 'picture']

class DrinksView(generic.ListView):
   template_name = 'wizapp/drinks.html'
   context_object_name = 'all_drinks'

   def get_queryset(self):
       return Drink.objects.all()
'''

def index(request):
    return HttpResponse("Hello, world. You're at the wizards new home.")

'''