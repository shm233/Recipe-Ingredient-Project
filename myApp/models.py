from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    def __str__(self):
        return self.username

class RecipeModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    recipe_image = models.ImageField(upload_to='media/recipe', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class IngredientModel(models.Model):
    recipe = models.ForeignKey(
        RecipeModel,
        on_delete=models.CASCADE,
        null=True,
        related_name='recipes')
    name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name
