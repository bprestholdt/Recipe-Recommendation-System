from django.test import TestCase
from django.contrib.auth.models import User
from databaseManager.models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.recipe = Recipe.objects.create(
            title='Pasta',
            description='Delicious pasta recipe',
            author=self.user,
            ingredients='Tomatoes, Basil, Garlic',
            instructions='Boil pasta, make sauce, mix together.'
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Pasta')
        self.assertEqual(self.recipe.description, 'Delicious pasta recipe')
        self.assertEqual(self.recipe.author, self.user)
        self.assertEqual(self.recipe.ingredients, 'Tomatoes, Basil, Garlic')
        self.assertEqual(self.recipe.instructions, 'Boil pasta, make sauce, mix together.')
