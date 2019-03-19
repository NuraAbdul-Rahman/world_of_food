from haystack import indexes
from breakfast.models import Recipe

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    recipe_name = indexes.CharField(model_attr='recipe_name', faceted=True)
    continent = indexes.CharField(model_attr='continent', faceted=True)
    labels = indexes.CharField(model_attr='labels', faceted=True)
    ingredients = indexes.CharField(model_attr='ingredients')
    short_description = indexes.CharField(model_attr='short_description')
    
    
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Recipe

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
