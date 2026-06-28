from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', signupPage, name='signup'),
    path('login/', signinPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('recipe/', recipe_list, name='recipe'),
    path('add-recipe/', add_recipe, name='add_recipe'),
    path('update-recipe/<str:r_id>/',update_recipe, name='update_recipe'),
    path('delete-recipe/<str:r_id>/', delete_recipe, name='delete_recipe'),
    path('ingredients/', ingredient_list, name='ingredient_list'),
    path('add-ingredients/', ingredient_add, name='ingredient_add'),
    path('update-ingredients/<str:i_id>', ingredient_update, name='ingredient_update'),
    path('delete-ingredients/<str:i_id>', ingredient_delete, name='ingredient_delete'),
]
