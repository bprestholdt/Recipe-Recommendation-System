from django.shortcuts import render
from django.http import HttpResponse
from databaseManager.models import Recipe
from databaseManager.forms import RecipeForm

recipes = [
  {
    'author': 'Harold',
    'title': 'Meatballs',
    'ingredients': 'meat in ball shape, salt, oil',
    'date_posted': 'April 18th, 2024'
  },
  {
    'author': 'Bodybuilder Brad',
    'title': 'Pb & J',
    'ingredients': 'peanut butter, jelly, bread, Trenbolone',
    'date_posted': 'May 24th, 2022'
  },
  {
    'author': 'Yukon Cornelius',
    'title': 'Lollipop',
    'ingredients': 'icicle, peppermint',
    'date_posted': 'January 2nd, 1964'
  }
]

# Create your views here.

#example function to be integrated w gpt
def generate_recipe_chatGPT(ingredients):
    # call api or gpt function here
    # placeholder returns example recipe
    return {
        'author': 'Generated Author',
        'title': 'Generated Recipe',
        'ingredients': ingredients,
        'date_posted': 'Today'
    }
#function to save recipe to user account in postgreSQL database
def save_recipe(title, description, ingredients, author):
    recipe = Recipe(
        title=title,
        description=description,
        ingredients=ingredients,
        author=author  # add recipe to user account
    )
    recipe.save() #save recipe to database using method from databaseManager
    
    

def home(request):
    if request.method == 'POST':
        # Handle submitted recipe
        form = RecipeForm(request.POST)
        if form.is_valid():
            #generate recipe with gpt
            # generate recipe w gpt function
            gpt_generated_recipe = generate_recipe_chatGPT(form.cleaned_data['ingredients'])

        # Create a new instance of the Recipe model with the generated recipe
            recipe = Recipe(
                title=gpt_generated_recipe['title'],
                description=gpt_generated_recipe['description'],
                ingredients=form.cleaned_data['ingredients'],
                author=request.user
            )
        # Save the new recipe to the database (and tie to user account)
            recipe.save()

            # Redirect to a success page or render a success message
            return render(request, 'pages/success.html')
        
        else:
            form = RecipeForm()



        context = {
            'recipes': recipes,
            'recipe': gpt_generated_recipe if request.method == 'POST' else None  # Only show generated recipe if ingredients are input
        }
    else:
        context = {
        'recipes': recipes,
        'recipe': None
    }
    return render(request, 'pages/home.html', context)