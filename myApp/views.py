from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myApp.models import *
from django.contrib.auth.decorators import login_required

def signupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pro_picture = request.FILES.get('picture')
        password = request.POST.get('password')
        confirm_password = request.POST.get('passwordc')
        
        user_exist = Custom_User.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, "User Exists")
            return redirect('signup')
        
        if password==confirm_password:
            
            Custom_User.objects.create_user(
                username=username,
                password=password,
                email=email,
                profile_pic = pro_picture,
                )
            messages.success(request, "Account created successfully.")
            return redirect("login")
    return render(request, 'auth/signup.html')

def signinPage(request):

    if request.method == "POST":

        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("recipe")
        else:
            messages.warning(request, "User not found")
            return redirect('login')
    return render(request,'auth/login.html')

@login_required
def logoutPage(request):

    logout(request)
    return redirect('login')


def recipe_list(request):
    recipe = RecipeModel.objects.all()
    context = {
        'recipe' : recipe
    }
    return render(request, 'recipe/recipe.html', context)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        recipe_image = request.FILES.get('recipe_image')
        
        RecipeModel.objects.create(
            name = name,
            description = description,
            category = category,
            recipe_image = recipe_image
        )
        messages.success(request, 'New Recipe Added')
        return redirect('recipe')
    return render(request, 'recipe/add-recipe.html')

@login_required
def update_recipe(request, r_id):
    recipe = RecipeModel.objects.get(id = r_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        recipe_image = request.FILES.get('recipe_image')
        
        recipe.name = name
        recipe.description = description
        recipe.category = category
        if recipe_image:
            recipe.recipe_image = recipe_image
        recipe.save()
        messages.success(request, 'Data Updated Successfully')
        return redirect('recipe')
    context ={
        'recipe' : recipe
    }
    return render(request, 'recipe/update-recipe.html', context)

@login_required
def delete_recipe(request, r_id):
    RecipeModel.objects.get(id = r_id).delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect('recipe')

def ingredient_list(request):
    ingredient_data = IngredientModel.objects.all()
    context = {
        'ig_data' : ingredient_data
    }
    return render(request, 'ig/ingredient.html', context)

@login_required
def ingredient_add(request):
    recipe_data = RecipeModel.objects.all()
    
    if request.method == 'POST':
        recipe = request.POST.get('recipe')
        name = request.POST.get('name')
        quantity = int(request.POST.get('quantity'))
        unit_price = float(request.POST.get('unit_price'))
        
        recipes = RecipeModel.objects.get(id = recipe)
        cost = quantity * unit_price
        
        IngredientModel.objects.create(
            recipe = recipes,
            name = name,
            quantity = quantity,
            unit_price = unit_price,
            cost = cost
        )
        messages.success(request, 'Ingredient Added Successfully')
        return redirect('ingredient_list')
    context = {
        'recipe_data' : recipe_data
    }
    return render(request, 'ig/ig-add.html', context)

@login_required
def ingredient_update(request, i_id):
    rec = RecipeModel.objects.all()
    ingredient = IngredientModel.objects.get(id = i_id)
    
    if request.method == 'POST':
        recipe = request.POST.get('recipe')
        name = request.POST.get('name')
        quantity = int(request.POST.get('quantity'))
        unit_price = float(request.POST.get('unit_price'))
        
        recipes = RecipeModel.objects.get(id = recipe)
        cost = quantity * unit_price
        
        ingredient.recipe = recipes
        ingredient.name = name
        ingredient.quantity = quantity
        ingredient.unit_price = unit_price
        ingredient.cost = cost
        ingredient.save()
        messages.success(request, 'Data Update Successfully')
        return redirect('ingredient_list')
        
    context = {
        'ingredient' : ingredient,
        'rec' : rec
    }
    return render(request, 'ig/ig-update.html', context)

@login_required
def ingredient_delete(request, i_id):
    
    IngredientModel.objects.get(id = i_id).delete()
    messages.success(request, "Data deleted successfully")
    return redirect('ingredient_list')
