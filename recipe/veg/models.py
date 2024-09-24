from django.db import models
from django.contrib.auth.models import User

class veg_recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=50, null=False, blank=False) 
    recipe_procedure = models.TextField(max_length=2000, null=False, blank=False)  
    recipe_image = models.ImageField(upload_to='media', null=True, blank=True)  
