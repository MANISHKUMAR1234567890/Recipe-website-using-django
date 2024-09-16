from django.db import models

class veg_recipe(models.Model):
    recipe_name=models.CharField(max_length=50, default=None)
    recipe_procedure=models.TextField(max_length=2000)
    recipe_image=models.ImageField(upload_to='media')