from haystack import indexes
from breakfast.models import Recipe

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    recipe_name = indexes.CharField(model_attr='recipe_name')
    continent = indexes.CharField(model_attr='continent')
    keywords = indexes.CharField(model_attr='keywords')
    ingredients = indexes.CharField(model_attr='ingredients')
    short_description = indexes.CharField(model_attr='short_description')
    slug = indexes.CharField(model_attr='slug')
    continent_slug = indexes.CharField(model_attr='slug')

    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Recipe

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
