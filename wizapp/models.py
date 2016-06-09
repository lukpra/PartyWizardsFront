from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):
    name =  models.CharField(max_length=250)
    recipe = models.CharField(max_length=1000)
    picture = models.FileField()

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
    barcode = models.IntegerField(max_length=20)

class ListIngredients(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=5)
    kindMeasure = models.CharField(20)

class ListTools(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

class ListDecoration(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)

class Rating(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    rating = models.IntegerField(max_length=2);

class Answer(models.Model):
    comment = models.CharField(max_length=1000)
    date = models.DateField()
    delete = models.BooleanField()

class Comment(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    comment = models.CharField(max_length=1000)
    date = models.DateField()
    delete = models.BooleanField()

class Ban(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    perm = models.BooleanField()

class myUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_moderator = models.BooleanField()
    date_of_birthday = models.DateField()
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
