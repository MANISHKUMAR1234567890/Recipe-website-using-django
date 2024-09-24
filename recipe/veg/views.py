from django.shortcuts import render,redirect
from veg.models import *
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

@login_required(login_url='login_page')
def Recipe(request):
    if request.method=='POST':
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')


        recipe_name=data.get('recipe_name')
        recipe_procedure=data.get('recipe_procedure')


        veg_recipe.objects.create(
            recipe_name=recipe_name,
            recipe_procedure=recipe_procedure,
            recipe_image=recipe_image,
            )
        
        return redirect('Recipe')
        

    query=veg_recipe.objects.all()
     
    if request.GET.get('search'):
        query=query.filter(recipe_name__icontains=request.GET.get('search'))


    context={'Recipe':query}
    

    return render(request,'recipe.html',context)


   
def delete_recipe(request, id):
    queryset=veg_recipe.objects.get(id=id)
    queryset.delete()

    return redirect("Recipe")

def update_recipe(request,id):
    queryset=veg_recipe.objects.get(id=id)

    if request.method=='POST':
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')


        recipe_name=data.get('recipe_name')
        recipe_procedure=data.get('recipe_procedure')
        
        queryset.recipe_name=recipe_name,
        queryset.recipe_procedure=recipe_procedure,
        if recipe_image:
            queryset.recipe_image=recipe_image
        
        queryset.save()
        return redirect('Recipe')
    context={'recipe':queryset}

    return render(request,'update_recipe.html',context)



def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passward=request.POST.get("passward")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid username.")
            return redirect('login_page')
        
        
        
        user=authenticate(request, username=username, password=passward)

        if user is not None:
            login(request,user)
            return redirect('Recipe')
        else:
            messages.error(request,"Wrong password!")
            return redirect("login_page")
           


    return render(request,'login.html')




def register_page(request):
    if request.method=='POST':
        

        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        passward=request.POST.get('passward')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"Username already taken.")
            return redirect('register_page')
        
            

        user=User.objects.create(
            first_name=first_name,
            email=email,
            username=username
        )
        passward=user.set_password(passward)
        user.save()

        messages.info(request,"Account created successfully.")

        return redirect('register_page')

    return render(request,'register.html')



def logout_page(request):
    logout(request)
    return redirect('login_page')


