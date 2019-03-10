import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'World_Of_Food.settings')

import django 
django.setup()
from breakfast.models import Continent, Recipe

def populate():

        north_america_recipes =[
                {"recipe_name": "Pancakes",
                "short_description": "Some lovely pancakes",
                "description": "Loads of lovely pancakes",
                "ingredients": "panacakes",
                "steps": "1. Make pancakes.\n2. Eat pancakes",
                "views": 0, "likes": 0, "image": "pancakes.jpg"} ]

        latin_america_recipes = [
                {"recipe_name": "Hot Chilli Flakes",
                "short_description": "Really hot",
                "description": "They really are very hot",
                "ingredients": "Chilli",
                "steps": "1.Mixed up the chilli",
                "views": 0, "likes": 0, "image": "ChilliFlakes.jpg"} ]

        africa_recipes = [
                {"recipe_name": "Special Museli",
                "short_description": "Museli with special stuff",
                "description": "Very special museli with extra special stuff",
                "ingredients": "museli",
                "steps": "1. Mix it up.\n2. Add some milk",
                "views": 0, "likes": 0, "image": "museli.jpg"} ]

        europe_recipes = [
                {"recipe_name": "Bacon and eggs",
                "short_description": "Bacon served with eggs",
                "description": "Bacon and Eggs",
                "ingredients": "Bacon and eggs",
                "steps": "1. Cook the bacon and the eggs",
                "views": 0, "likes": 0, "image": "bacon.jpg"} ]

        asia_recipes = [
                {"recipe_name": "Hong Kong Wonton Soup", 
                "short_description": "Wontons and dumplings are two similar types of food, "
                "which are comprised of a square or round wrapper (a dough skin made of flour and water)"
                "and fillings. Wontons can be boiled in a fragrant and watery broth, steamed in a bamboo "
                "steamer, or fried in a high-heat wok. Sometimes, wontons are also served with little noodles" 
                "to make 'wonton noodles'. They are available with a large variety of fillings, such as" 
                "ground pork, shrimp, fish, mushrooms, and other vegetables.", 
                "description": "Homemade wonton soup!" 
                "These wontons are filled with a juicy pork and prawn / shrimp filling and will knock your socks off." 
                "With step by step photos and a recipe video, you're going to be a Wonton Wrapping Master in no time!"
                "Added bonus:  Best standby freezer meal ever and super healthy (350 calories for a bowl!)"   
                "If you've ever had store bought frozen wontons or wontons from a good value Chinese place that probably"
                "uses frozen wontons, you will be amazed how different homemade ones are. The main difference is the texture" 
                "of the filling because homemade wontons are made with just pure fresh ingredients, NO mysterious fillers!"
                "I think wontons are one of those things that many people don't think to make, assuming they are really tedious and take ages." 
                "But they don't!! The wonton filling takes minutes to make (literally 5 minutes) and wrapping the wontons is quite fast if you use my method!",
                "ingredients": "50 - 60 wonton wrappers\nWONTON FILLING\n200 g / 7 oz lean pork mince (ground pork)\n200 g / 7 oz peeled prawns / shrimp , roughly chopped"
                "\n1 tbsp ginger , finely grated (3cm piece)\n2 shallots / green onions , finely chopped (5 tbsp)\n1 tbsp light soy sauce (1)"
                "2 tbsp Chinese cooking wine (Shaoxing wine) (2)\n1/2 tsp salt\n2 tbsp sesame oil (3)\nBROTH (FOR 2 SERVINGS)\n"
                "3 cups / 750 ml chicken broth (5)\n2 garlic cloves , smashed (6)\n1 1/2 cm piece of ginger , sliced (optional, but highly recommended)"
                "1 tbsp light soy sauce (1)\n2 tsp sugar (any)\n1 tbsp chinese cooking wine (2)\n1 tsp sesame oil\nTO SERVE"
                "Shallots / scallions, finely chopped\nBok choy , quartered, or Chinese broccoli cut into 10cm lengths (optional)\n"
                "40 - 50 g / 1.5 - 1.75 oz dried egg noodles per person, (optional) (8)", 
                "steps": "1. Place Filling ingredients in a bowl. Use a potato masher to mash"
                "until fairly smooth - about 20 mashes. Don't turn the prawn into a complete paste, small chunks are good.\nWRAPPING (SEE PHOTOS AND VIDEO):\n"
                "1. Use My Way (better Wonton Soup experience!) or the Asian Grocery Store Way (easier to pack for freezing).\n2. Lay Wontons on work surface."
                "Use 2 teaspoons to put the Filling on the wontons. Work in batches of 5 if starting out, up to 15 or 20 if confident. Brush 2 edges with water."
                "Fold to seal, pressing out air. Brush water on one corner and bring corners together, pressing to seal.\n3. Place wrapped wontons into a container with"
                "a lid as you work (so they don't dry out).\nCOOKING/FREEZING:\n1. To cook: bring a large pot of water to boil. Place wontons in water and cook for 4 minutes"
                "or until they float. Remove with slotted spoon straight into serving bowls. Ladle over broth.\n2. To freeze: Freeze uncooked in airtight containers. Cook from"
                "frozen for 6 to 8 minutes. IMPORTANT: Do not freeze if you made this with defrosted frozen prawns. (Note 11)\nBROTH:\n1. Place Broth ingredients in a saucepan"
                "over high heat. Add white ends of scallions/shallots if leftover from Wonton filling.\n2. Place lid on, bring to simmer then reduce to medium high and simmer" 
                " for 5 - 10 minutes to allow the flavours to infuse. Pick garlic and ginger out before using.\n3. If using vegetables, blanch in the soup broth and place in serving bowl."
                "\nASSEMBLE SOUP:\n1. Prepare noodles according to packet directions (if using noodles). Place in serving bowl with cooked wontons and blanched vegetables.\n"
                "2. Ladle over soup. Serve!", "views": 0, "likes": 0, "image": "HongKong-WontonSoup.jpg"} ]
        
        oceania_recipes = [
                {"recipe_name": "vegemite on toast",
                "short_description": "vegemite on toast",
                "description": "It's vegemite on toast",
                "ingredients": "Vegemite, bread, butter",
                "steps": "1. Toast bread.\n2. Spead butter.\n3. Spread vegemite",
                "views": 0, "likes": 0, "image": "vegemite.jpg"} ]

        Continents = {"North America": {"recipes": north_america_recipes},
                        "Latin America": {"recipes": latin_america_recipes},
                        "Africa": {"recipes": africa_recipes},
                        "Europe": {"recipes": europe_recipes},
                        "Asia": {"recipes": asia_recipes},
                        "Oceania": {"recipes": oceania_recipes}} 

        for cont, cont_data in Continents.items():
                c = add_continent(cont)
                for r in cont_data["recipes"]:
                        add_recipe(r["recipe_name"], c, r["short_description"], r["description"], r["ingredients"], r["steps"], r["views"], r["likes"], r["image"])

        for cont in Continent.objects.all():
                for r in Recipe.objects.filter(continent=cont):
                      print("- {0} - {1}".format(str(cont), str(r)))    

def add_continent(name, views=0):
        c = Continent.objects.get_or_create(name=name)[0]
        c.views = views
        c.save()
        return c

def add_recipe(recipe_name, continent, short_description, description, ingredients, steps, views, likes, image):
        r = Recipe.objects.get_or_create(recipe_name=recipe_name, continent=continent)[0]
        r.short_description = short_description
        r.description = description
        r.ingredients = ingredients
        r.steps = steps
        r.views = views
        r.likes = likes
        r.image = image
        r.save()
        return r

if __name__=='__main__':
        print("Starting breakfast population script...")
populate()

        

