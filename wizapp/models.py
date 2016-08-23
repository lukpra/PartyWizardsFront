from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Drink(models.Model):
    name =  models.CharField(max_length=250)
    recipe = models.CharField(max_length=1000)
    picture = models.FileField()

    def get_absolute_url(self):
        return reverse('wizapp:drinks', kwargs={'pk': self})

    def __str__(self):
        return self.name



class Ingredient(models.Model):
    name =  models.CharField(max_length=250)
    kind = models.CharField(max_length=250)

class Tool(models.Model):
    name = models.CharField(max_length=250)
    kind = models.CharField(max_length=250)
    picture = models.FileField()

class Decoration(models.Model):
    name = models.CharField(max_length=250)
    picture = models.FileField()

class Barcode(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    barcode = models.IntegerField()

class ListIngredients(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    kindMeasure = models.CharField(max_length=20)

class ListTools(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

class ListDecoration(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)

class Rating(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    rating = models.IntegerField();

class Comment(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    delete = models.BooleanField(default=False)

class Answer(models.Model):
    answer_comment = models.ForeignKey(Comment)
    comment = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    delete = models.BooleanField(default=False)

class Ban(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    perm = models.BooleanField(default=False)

class myUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)
    date_of_birthday = models.DateField()
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
