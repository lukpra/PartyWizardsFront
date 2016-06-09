from django.contrib import admin
from .models import Drink, Ingredient, Tool, Rating, Decoration, Barcode, ListIngredients, ListDecoration, ListTools, Comment, Answer, Ban, myUser

# Register your models here.
admin.site.register(Drink)
admin.site.register(Tool)
admin.site.register(Ingredient)
admin.site.register(Decoration)
admin.site.register(Barcode)
admin.site.register(ListIngredients)
admin.site.register(ListDecoration)
admin.site.register(ListTools)
admin.site.register(Ban)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Rating)
