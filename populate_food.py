
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'World_Of_Food.settings')

import django 
django.setup()
from breakfast.models import Continent, Recipe

def populate():

        north_america_recipes =[
                {"text": "breakfast", "recipe_name": "Pancakes",
                "short_description": "Some lovely pancakes",
                "description": "Loads of lovely pancakes",
                "ingredients": "panacakes",
                "steps": "1. Make pancakes.\n2. Eat pancakes",
                "keywords": "vegetarian",
                "views": 0, "likes": 0, "image": "pancakes.jpg"} ]

        latin_america_recipes = [
                {"text": "breakfast", "recipe_name": "Ham and Cheese Empanadas",
                "short_description":"Although these are not traditional empanadas because they are made with puff "
                "pastry dough, they are still very popular, especially for breakfast. They are often "
                "shaped as a square, maybe to distinguish them from the classic round empanadas.",
                "description": "The light and flaky pastry combines perfectly with the melted cheese and ham. If\nyou've been resorting to commercially-prepared hot pockets for quick breakfasts, " 
                "lunches, and snacks, this can be your go-to alternative. You can make these\n empanadas and freeze them unbaked, then take them straight from the freezer to "
                "the oven for a quick hot treat.",
                "ingredients": "2 tablespoons butter\n1/2 cup flour\n1 cup milk\n2 eggs"
                "1/2 cup cheese (grated smoked gouda, edam, or similar)\n4 tablespoons parmesan (grated)"
                "1 pinch cayenne pepper\n1 pinch salt (to taste)\n1 package puff pastry dough (frozen)"
                "1/4 pound ham (deli)\n1 egg yolk\n1 tablespoon water​",
                "steps": "1. Gather the ingredients\n2. Preheat oven to 400 F.\n3. In a saucepan, melt butter over medium-low heat."
                "4. Whisk the flour into the melted butter, and increase the heat to medium. Cook, stirring, for 1 to 2 minutes."
                "5. Whisk the milk into the flour/butter mixture and bring it to boil, stirring. The sauce will thicken slightly."
                "6. Whisk 2 eggs into mixture and cook, stirring, for 1 to 2 minutes more or until sauce has thickened."
                "7. Add grated cheese and parmesan and stir until melted. Remove from heat and add cayenne pepper and salt to taste."
                "8. Roll out 1 sheet of puff pastry dough on a floured surface to 12 inches square. With a pizza cutter or sharp knife, cut dough into 12 3-inch-by-4-inch rectangles."
                "9. Mix the egg yolk with the water, and brush the edges of half of the rectangles with the egg yolk mixture."
                "10. Place a piece of ham in the center of each rectangle that has been brushed with the egg yolk mixture. "
                "There should be an edge of dough all around the ham. Top ham the ham with 2 tablespoons of the cheese mixture."
                "11. Cover the ham and cheese with one of the plain rectangles, and firmly press down around the edges to seal."
                "12. Cover the ham and cheese with one of the plain rectangles, and firmly press down around the edges to seal."
                "13. When ready to bake, prick the top of the empanadas several times with a fork, and brush tops lightly with the egg yolk mixture."
                "14. Bake 20 minutes, or until puffed and golden brown.\n15. Serve hot or at room temperature.",
                "keywords": "meat",
                "views": 7, "likes": 3, "image": "Ham&Cheese Empanadas.jpg"},
                {"text": "breakfast", "recipe_name": "Homemade South American Arepas",
                "short_description": "Arepas, a staple food in both Venezuela and Colombia, are corncakes that are \nmade from a special precooked corn flour. You can find this cornmeal/flour in Latin food "
                "stores, labeled masarepa, or 'masa al instante.'",
                "description": "Arepas are scrumptious slathered with butter or cream cheese for breakfast or as an accompaniment to any meal."
                "Colombian arepas tend to be thinner than the Venezuelan variety. \nVenezuelan arepas are often stuffed with meat and cheese to make sandwiches, "
                "such as the famous reina pepiada. Arepas can also be grilled or deep-fried and are \nsometimes prepared with other grains such as fresh corn, hominy or quinoa.",
                "ingredients": "1 teaspoon salt\n2 1/2 cups masarepa cornmeal\n2 3/4 to 3 1/2 cups hot water"
                "2 tablespoons melted vegetable butter\n1/2 tablespoon vegetable butter or vegetable oil",
                "steps": "1. Stir the salt into the masarepa cornmeal.\n2. Pour 2 3/4 cups of hot water over the flour and mix well with a wooden spoon."
                "3. Stir in the melted butter. Cover dough with plastic wrap and let rest 15 minutes. \n4. If you want thicker arepas, separate the dough into 12 pieces."
                "5. Shape each piece into a smooth ball.  Add more water if needed -- the dough should be"
                "moist enough so that you can shape the arepas without the dough forming lots of cracks around the edges."
                "6. Place each ball in between 2 sheets of plastic wrap or 2 ziplock bags and flatten gently with the bottom of a pot."
                "7. Use your fingers to smooth out any cracks along the edges.\n8. Place the shaped arepas on a cookie sheet covered with plastic wrap."
                "9. Heat a cast iron skillet on low heat. Put 1/2 tablespoon butter or vegetable oil in the skillet."
                "10. Place several arepas in the pan, leaving room to turn them."
                "11. Cook the arepas about 5 minutes on each side. The surface should dry and form a crust."
                "12. The thinner arepas are done when they have formed a nice crust but are still soft on the inside."
                "13. The thicker, Venezuelan-style arepas finish cooking in the oven. After they have formed a crust "
                "and are just a bit browned, place them on a cookie sheet and heat for 8 to 10 minutes at 350 F."
                "13. Serve both thin and thick arepas hot.",
                "keywords": "vegetarian",
                "views": 12, "likes": 5, "image": "HomemadeSouthAmericanArepas.jpg"},
                {"text": "breakfast", "recipe_name": "Rosca de Coco: Braided Coconut Ring",
                "short_description": "This sweet braided bread ring has a creamy coconut filling and sugary glaze. "
                "The dough is buttery and brioche-like, similar to sweet roll dough, and is very easy to work with.",
                "description": "In addition to a braided ring, the dough can be shaped in the same manner as "
                "cinnamon rolls - by rolling the dough out into a large rectangle, spreading most of "
                "the filling over the dough, rolling it into a cylinder, and cutting the cylinder into "
                "spiral slices. Place the rolls in a 9x13 inch pan to rise and bake, then glaze the rolls "
                "with the remaining filling when they are out of the oven. "
                "Any leftovers are especially tasty when toasted and spread with butter. ",
                "ingredients": "For the Dough:\n1 cup milk\n1/4 ​coconut cream\n3/4 cup sugar\n5 tablespoons butter"
                "2 teaspoons active dry yeast\n3 eggs\n1/2 teaspoon salt (or to taste)\n1 teaspoon vanilla"
                "1/2 teaspoon coconut flavoring\n4 1/2 to 5 cups all-purpose flour"
                "For the Filling/Glaze:\n1 1/2 cups coconut (sweetened shredded)\n4 tablespoons butter"
                "1 can condensed milk\n1/2 cup cream\n12 teaspoon coconut flavoring\n1 pinch salt\n1 egg",
                "steps": "1. Preheat the oven to 300 degrees.  Place the shredded coconut in a shallow baking dish " "and toast in the oven, stirring occasionally, until golden brown.  Once cool, place the coconut in a" "food processor and pulse briefly to finely chop (or chop by hand).  Set aside."
                "2. Place the milk in a small saucepan with the cream of coconut and the "
                "sugar. bring the mixture to a simmer, then remove from heat. "
                "3. Place the butter in the bowl of a standing mixer fitted with the dough hook attachment. "
                "Pour the warm milk and sugar mixture over the butter and let cool briefly."
                "4. Add the eggs, 1 cup of flour, the salt, the vanilla, and the coconut flavoring, and mix on low "
                "speed until flour is incorporated. Add 3 more cups of flour, 1 cup at a time, and mix well."
                "5. Transfer dough to an oiled bowl and cover loosely. Set dough aside to rise in a warm place for about an hour. "
                "6. Place the condensed milk, 3 tablespoons butter, cream, toasted coconut, and a pinch of salt into a small saucepan. "
                "7. Shape the braided ring:  Turn dough out onto a lightly floured surface and divide the dough into 3 equal pieces. "
                "8. Extend each piece of dough into a long cylinder by rolling it on the counter, "
                "with your hands starting in the middle and rolling out to each side. "
                "9. Loosely braid the 3 pieces of dough then attach the ends to form a ring. "
                "10. Crack the egg into a small bowl and mix with 1 tablespoon of water.  Brush the egg wash over the braid.  "
                "11. Bake the bread until it is golden brown and puffed, about 40-45 minutes.  "
                "12. Serve warm or at room temperature. ",
                "keywords": "vegetarian",
                "views": 6, "likes": 1, "image": "RoscaDeCoco.jpg"},
                {"text": "breakfast", "recipe_name": "Sausage and Egg Breakfast Casserole",
                "short_description": "This overnight breakfast (or brunch) casserole is full of flavor, with eggs, bread, "
                "sausage, cheese, and seasonings. It's the perfect egg casserole recipe for a holiday or weekend morning meal.",
                "description": "One thing that makes this casserole and other similar casseroles so perfect for a busy "
                "weekend or holiday morning is that it is prepared the night before. All you have to do in the morning "
                "is remove it from the refrigerator, let it stand to warm up a bit, and then pop it into a preheated oven."
                "Serve it along with fresh diced or sliced melon or grapes, or a warmed fruit compote mixture. "
                "Sliced tomatoes go nicely with egg dishes as well.",
                "ingredients": "7 slices white bread (crusts removed, or use Italian bread)\n1 tablespoon butter (softened)"
                "1 pound ground sausage\n4 cups cheddar cheese (shredded)\n6 large eggs\n1 teaspoon salt"
                "1 teaspoon dry mustard\n2 cups half and half (or milk)",
                "steps": "1.Gather ingredients.\n2. Lightly butter each slice of bread and then cut the slices in half. "
                "Arrange the bread slices in a 9-by-13-by-2-inch baking pan."
                "3. In a large skillet or saute pan, brown the sausage. Use a spatula or spoon to break it up. Drain and pat with paper towels."
                "Sprinkle the sausage over the bread. Top the sausage with the shredded cheese."
                "4. In a mixing bowl, whisk together the eggs, salt, dry mustard, and the milk until well blended. Pour" "egg mixture over bread, sausage, and cheese."
                "5. Cover the pan with foil and refrigerate overnight."
                "6. Remove the casserole from the refrigerator and let it stand at room temperature for about 20 minutes."
                "7. Preheat the oven to 350 F."
                "8. Remove the foil from pan and bake the casserole for 45 minutes, or until it is bubbly around the edges "
                "and lightly browned on top. It might take a bit longer if it's still quite cold. "
                "9. Remove the breakfast casserole to a rack and let it stand for 15 to 20 minutes before serving."
                "10. Serve and enjoy!",
                "keywords": "meat",
                "views": 18, "likes": 7, "image": "Sausage&EggBreakfastCasserole.jpg"},
                {"text": "breakfast", "recipe_name": "Venezuelan Perico",
                "short_description": "Perico is a savory Venezuelan breakfast dish of scrambled eggs seasoned with "
                "sauteed onions, tomatoes, and peppers. It's often served inside arepas, a "
                "Venezuelan egg McMuffin of sorts.",
                "description": "If you don't want to make arepas, serve with corn or poppyseed muffins, English "
                "muffins or multigrain or whole wheat toast. A side of bacon or sausage, just like "
                "with any egg dish, makes a nice addition for a weekend breakfast or brunch."
                "Perico means parakeet in English. Some believe the name for this dish derives from "
                "its colorful presentation of the red in the tomatoes, the green in the pepper and "
                "the yellow of the eggs. Perico is made most often at home, and every family has its "
                "own version it likes best, similar to omelets in the U.S.",
                "ingredients": "4 to 6 eggs\n3 tablespoons cream\n2 tablespoons butter\n1 tablespoon vegetable oil"
                "1 medium onion, chopped fine\n1 medium tomato, chopped fine\nOptional: 1 green pepper, chopped fine"
                "Salt and pepper to taste",
                "steps": "1. Whisk the eggs together with the cream. Set aside."
                "2. Melt the butter with the oil in a large nonstick skillet."
                "3. Add the chopped onions to the pan and saute over medium heat until they are translucent."
                "4. Add the tomatoes and green pepper and cook over medium heat until soft, 8 to 10 minutes."
                "5. Pour the egg and cream mixture into the skillet and cook gently, stirring them lightly and flipping them as they cook."
                "6. Cook the eggs to the desired doneness and season with salt and pepper to taste."
                "7. Serve warm with arepas or other bread choices.",
                "keywords": "vegetarian",
                "views": 5, "likes": 2, "image": "VenezuelanPerico.jpg"} ]
        
        africa_recipes = [
                {"text": "breakfast", "recipe_name": "Hausa Koko",
                "short_description": "Hausa Koko, a soured and spicy smooth porridge.",
                "description": "Hausa Koko is simply a thick flowing tasty solution made from millet with a few local spices added to give it a particular taste and colour.\n It is called “Hausa Koko” because of it’s popularity in the northern areas and is believed to have been first made by the Hausas. Sugar,milk and groundnuts are added to give it a very delicious taste.\n Hausa Koko is mostly served with “Koose”, a millet based paste which is made into balls and fried in vegetable oil.",
                "ingredients": "1/2 cup corn dough \n 3 cups water (divided use)\n 1/4 teaspoon cloves \n 1/2 teaspoon ginger \n 1/4 teaspoon hot chilli powder \n Optional: sugar to taste \n 1 pinch salt",
                "steps": "1. Gather the ingredients.Scoop about 1/2 a cup of corn dough and place into a pan.\n 2. Add 1 cup of cold water and crumble up the corn dough to make a smooth paste with the water. Turn on the heat to high and stir continuously.\n 3.Add 2 cups of boiling water to the pot and bring to the boil whilst stirring continuously. At this point, the corn dough begins to thicken and form gelatinous looking lumps. I normally keep a whisk handy to aid in the smoothing out of the porridge.\n 4. Add a pinch of salt, the ground cloves, ginger, and pepper. Stir and allow to simmer for 10 minutes on a low heat.\n 5. When ready to serve, pour into a bowl, add the desired amount of sugar and stir. For an added touch of luxury, pour in some evaporated milk.",
                "keywords": "vegan",
                "views": 20, "likes": 15, "image": "hausakoko.jpg"},
                {"text": "breakfast", "recipe_name": "Mahamri (Swahili Doughnuts)",
                "short_description": "These are perfect for breakfast with a cup of tea, and go really well as an accompaniment to many meals especially grilled meats.",
                "description": "Mahamri is a favourite treat amongst Kenyan households especially in the coastal region.\n Mahamris are miniature with a bulging square or triangular dough which is fried until they attain a golden brown hue.\n They are great for breakfast when eaten with beans in coconut sauce or with a cup of chai.",
                "ingredients": "3 cups plain flour \n 1 cup coconut milk powder \n 3/4 cup warm milk \n 1 teaspoon ground cardamom \n 1 tablespoon instant yeast \n 1/4 cup warm water \n 1/2 cup sugar \n Oil for deep frying",
                "steps": "1. Mix the yeast, a pinch of sugar, a pinch of plain flour and the ¼ cup of warm water. Leave the yeast to rise (the addition of sugar and flour helps in the rising process). \n 2. Knead the flour, sugar, cardamom, coconut powder, warm milk and yeast mixture to form a smooth dough.\n 3. Let the dough rest in a warm place – preferably overnight or until double in size (the dough could rise in a few hours if you live in a warm climate).\n 4. Divide dough into 8 balls.\n 5. Roll each ball into a 6 inch circle and cut into quarters.\n 6. Pour the oil in a deep frying pan on medium heat. You want the oil hot enough when you start frying the dough.\n 7. Drop the three to four triangles into the hot oil. If the oil is hot enough the dough will quickly float to the top and puff up. \n 7. Turn the mahamri as soon as it is a light brown and turn.\n 8. Cook on the other side for another minute and remove from the deep fryer with a slated spoon.\n 8. The doughnuts should be a light golden brown.",
                "keywords": "vegetarian, meat",
                "views": 13, "likes": 10, "image": "mahamri.jpg"},
                {"text": "breakfast", "recipe_name": "Baked Plantains & Egg Muffin",
                "short_description": "Baked Plantain Frittata aka  plantain and eggs- A healthier  and delicious take on fried plantains and eggs",
                "description": "Fried plantain and egg is one of my favorite weekend breakfast. It is one of the many traditional breakfasts found throughout West Africa.\n No one will ever guess that this nutritious, mouthwatering breakfast Frittata is lighter!\n Plantain makes  it a hearty, and the eggs and veggies pile on color and wonderful flavor.",
                "ingredients": "1 tablespoon canola oil & 1/2 medium onion thinly sliced. \n 1 scotch bonnet pepper diced sub hot sauce \n 1/2 red/green bell pepper stem, ribs, and seeds removed, then thinly sliced in strips \n 1 small tomatoes \n 1 teaspoon minced garlic & 1 teaspoon Fresh thyme or any herb \n 2-3 ripe plantains \n Coarse salt & ground pepper \n 6 large eggs \n 1 avocado optional \n optional: 1/2 -1 cup sausage chopped",
                "steps": "1. Adjust the oven rack to the middle position and preheat oven to 350 degrees F. Grease a 10- inch baking pan or muffin pan, set aside.\n 2. Using a sharp knife cut both ends off the plantain. This will make it easy to grab the skin of the plantains. Slit a shallow line down the long seam of the plantain, peel only as deep as the peel. Remove plantain peel by pulling it back. Slice the plantains into desired shape and size. \n 3. Place them on the baking sheets in a single layer; spray lightly over the plantains using the canola oil spray and bake, turning over slices, after 8 minutes for about 12- 20 minutes or till golden brown, depending on your oven. \n 4. While the plantains is baking, heat a medium sauce pan over medium high heat and drizzle with 1 Tablespoons of canola oil. Add the onions, tomatoes, green pepper and cook for about 4-5 minutes.\n 5. In a large bowl whisk eggs, add sauté vegetable mixture, season with salt and pepper according to preference.\n 6.Pour mixture into a greased 10-inch baking pan. Layer the baked plantains and sprinkle the parsley in the baking pan.\n 7. Bake in the oven for about 30-40 minutes; until mixture is firm in the center.\n 8. Let it cool for a few minutes; top with avocado if desired",
                "keywords": "vegetarian, healthy",
                "views": 33, "likes": 20, "image": "bakedPlantainFrittata.jpg"},
                {"text": "breakfast", "recipe_name": "Shakshuka",
                "short_description": "Shakshuka is a popular breakfast in North Africa and the Middle East",
                "description": "Braising eggs in a flavoursome, aromatic sauce is all the rage. It is warming and comforting, ideal for the morning when you are not normally up for a great culinary challenge.\n In North Africa they have known this dish for many years. There, according to region, they have many variations on this theme, with sauces varying in spiciness, sweetness and sharpness.\n You can add preserved lemon to your shakshuka, harissa paste, olives or a salty ewe's cheese. \n A spicy sausage – such as merguez or chorizo – is also suitable.",
                "ingredients": "3 tbsp olive oil & 2 large onions, thinly sliced \n 2 red peppers, cut into long slices &2 green peppers, cut into long slices \n 4 garlic cloves, finely chopped \n 1/2 tsp cumin seeds & 1/2 tsp caraway seeds \n 1/2 tsp cayenne pepper & 1 tbsp tomato or red pepper purée \n 2 x 400g tins tomatoes & 1 small bunch fresh coriander, roughly chopped \n 1 small bunch fresh parsley, roughly chopped & 8 free-range eggs \n 85g/3oz feta, crumbled & 8 tbsp thick natural yoghurt or labneh \n salt & freshly ground black pepper",
                "steps": "1. Preheat oven to 375°F.Heat the oil in a large heavy skillet, preferably cast iron, over medium heat. Add the onions and zucchini, and sauté for 8–10 minutes until tender. Add the garlic and cook for 1 minute, then add the cumin, paprika and cayenne, and cook for 1 more minute.\n 2. Add the tomatoes, salt and pepper and simmer until the tomatoes have thickened, about 10 minutes. Stir in the cheese. \n 3.Gently crack the eggs into the skillet, spreading them evenly over the tomatoes. Season with a pinch of coarse salt, if desired. Transfer the skillet to the oven and bake until eggs are just set, 7–8 minutes (they will continue to cook for a couple of minutes after you remove them from the oven). Sprinkle with the fresh herbs and serve immediately. \n 4. Do Ahead Or Delegate: Halve and slice the onion and zucchini, slice the garlic, combine the dry spices, chop the tomatoes, or fully prepare the recipe without the eggs and refrigerate or freeze it.\n 5.Flavor Booster: Use smoked paprika instead of regular paprika. Serve with hot pepper sauce such as Tabasco, sriracha or harissa, if you have it.",
                "keywords": "vegetarian, spicy",
                "views": 33, "likes": 25, "image": "shakshuka.jpg"},
                {"text": "breakfast", "recipe_name": "Injera",
                "short_description": "Injera is a Flat round fermented sourdough bread- bread like no other, with a unique, slightly spongy texture",
                "description": "Injera is a Flat round fermented sourdough bread- bread like no other, with a unique, slightly spongy texture.\n Always present during mealtime, in countries like Ethiopia, Eritrea, Somalia, Yemen, Djibouti and Sudan with each country having it’s own variation.",
                "ingredients": "1 cup corn flour \n 2 1/2 cup sorghum or whole wheat \n 1 Tablespoon sugar & 1 Tablespoon dry yeast \n 1 1/4 cup warm water \n 4 cups all purpose flour \n 6 teaspoons baking powder \n 4 teaspoons salt \n 1/4 cup sugar \n 4 cups warm water",
                "steps": "1. Combine corn flour , sorghum or  whole wheat , sugar yeast and water , mix and let it rise for about an hour.\n 2. In Large bowl combine flour , salt, baking powder and sugar. \n 3. Add the starter mixture to the flour, thoroughly mix and start adding water a little at a time until water has been completely used up, thoroughly miss to eliminate any lumps. You may use the blender to aid in the process. \n 4. Let it rise for about 2 hours.",
                "keywords": "vegan",
                "views": 23, "likes": 20, "image": "injera.jpg"}]

        europe_recipes = [
                {"text": "breakfast","recipe_name": "Bacon and eggs",
                "short_description": "Bacon served with eggs",
                "description": "Bacon and Eggs",
                "ingredients": "Bacon and eggs",
                "steps": "1. Cook the bacon and the eggs",
                "keywords": "meat",
                "views": 0, "likes": 0, "image": "bacon.jpg"} ]

        asia_recipes = [
                {"text": "breakfast","recipe_name": "Hong Kong Wonton Soup", 
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
                "2. Ladle over soup. Serve!", 
                "keywords": "meat",
                "views": 10, "likes": 5, "image": "HongKong-WontonSoup.jpg"},
                {"text": "breakfast", "recipe_name": "Japanese Traditional Style Breakfast", 
                "short_description": "A traditional Japanese breakfast is likely different from any other kind of breakfast you'll ever experience. It consists of foods that make up"
                "a complete meal that one could conceivably enjoy at lunch or dinner.",
                "description": "Typically, a traditional Japanese breakfast consists of steamed rice, miso soup, a protein such as grilled fish, and various side dishes. Familiar side"
                " dishes may include tsukemono (Japanese pickles), nori (dried seasoned seaweed), natto (fermented soybeans), kobachi (small side dishes which usually consist of vegetables),"
                " and a green salad. Although a Japanese breakfast comprises what Westerners might view as a complete meal appropriate for lunch or dinner, it is not intended to be heavy or too "
                "filling. Portion sizes for breakfast are adjusted to meet one's appetite, and dishes tend to be lighter, for example, they tend not to be greasy, deep fried, or rich.",
                "ingredients": "3 1/2 oz short-grain rice\n2 tbsp mixed Japanese pickles, such as cucumber, daikon, cabbage\nFor the leek and potato miso soup:\n1 tbsp instant dashi (Japanese stock) or vegetable"
                "\nStock powder\n2 1/4 cups boiling water\n2 medium-sized potatoes, peeled and chopped into small cubes\n1 tbsp white miso paste\n1 spring onion, very finely chopped\nFor the fish:\n"
                "1-inch piece of fresh ginger, finely chopped\n1 spring onion, finely chopped\n2 tbsp soy sauce\n2 5-oz fillets of salmon\nFor the omelette (tamagoyaki):\n3 medium free-range eggs\n"
                "1 tsp sugar\n2 tsp soy sauce\n1 tsp bonito flakes or instant dashi powder (optional)\nvegetable oil for cooking",
                "steps": "1. Cook the rice according to the instructions.\nFor the miso soup:\n1. Put the instant dashi stock in a pan with the boiling water. Add the potato and simmer over medium heat for "
                "about six minutes, or until the potato is cooked.\n2. Ladle some soup from the pan into a bowl and dissolve the miso in it. Gradually return the miso mixture to the soup. Stir the soup gently "
                "but don't let it come to the boil once you've added the miso. Turn off the heat and add the chopped spring onion.\n3. Serve hot in small bowls.\nFor the fish:\n1. Mix the ginger, spring onion "
                "and soy sauce together and pour over the salmon fillets. Leave them to stand at room temperature for 15 minutes.\n2. Pour a little boiling water into the grill pan and place the fish on the grill "
                "rack above the water (this keeps it moist while it grills). Grill the fish under medium to high heat for about 5-6 minutes on each side, taking care not to overcook it.\nFor the omelette:\n1. Combine "
                "the eggs, sugar, soy sauce and bonito flakes (or instant dashi), if using, and mix the ingredients thoroughly.\n2. Heat a little vegetable oil in a small, non-stick frying pan over medium to high heat "
                "and add the egg mixture. Agitate the eggs, using a wooden spoon, so the texture of the omelette remains fluffy.\n3. When the eggs are half-cooked, fold the omelette in half, to make a semi-circle, then "
                "fold the curving section inwards to form a rectangle, and then fold the ends inwards until you have what looks like a little square package. This creates the distinctive layered effect, called tamagoyaki, "
                "characteristic of a Japanese omelette.\n4. Flip the 'package' over and cook for a further two minutes. Cut into quarters.\nTo serve:\nJapanese etiquette decrees that you place the bowl of rice on your left "
                "and the bowl of miso soup on your right. Serve the fish on a separate plate, the pickles in a small bowl, and the omelette on another small plate. Now test your hungover skills with chopsticks.",
                "keywords": "meat, fish",
                "views": 20, "likes": 13, "image": "JapaneseTraditionalStyleBreakfast.jpg"},
                {"text": "breakfast", "recipe_name": "Soy Milk and Chinese Fried Dough",
                "short_description": "This breakfast set usually appears together in Chinese socities. The two components soybean milk and fried dough are the most common breakfast combination. Some locals also like to have "
                "deep-fried dough sticks with rice congee.",
                "description": "Soybean milk is made with a blender. You can find freshly blended or boiled soy milk in disposable cups at most breakfast stalls. Deep-fried dough sticks are long, brown, deep-fried sticks of dough."
                " You can eat one as it is or dip it in some soybean milk, which has a better taste.If you can not find unsweetened soy milk, you can buy a soy milk maker.you can find dried soy beans at your local Asian mart. Soak "
                "them overnight and put them in the Soymilk maker the next morning. You’ll be rewarded with fresh, hot soy milk in minutes. So for the following part we will mainly introduce the making methods of fried dough.",
                "ingredients": "2 cups all-purpose flour\n1 egg\n1/2 teaspoon salt\n1½ teaspoons baking powder\n1 tablespoon milk\n2 tablespoons softened (NOT MELTED) butter\nabout 1/3 cup water (the exact amount changes based on the "
                "humidity in your kitchen; the dough should be very soft, but not sticking to the mixing bowl)\nNotes:\n1. The frying temperature must be kept at or slightly above 400 degrees.\n2. If the two halves come apart while frying, "
                "there are two possible culprits: you might be over-frying it, or you did not press the two parts tightly together enough.\n3. Before assembling the youtiao, the dough must be completely back to room temperature and very soft to the touch."
                "4. If you have leftovers after frying, freeze the cooked youtiao in a ziplock bag. Reheat them in the toaster over or oven until just warmed through.\n5. Don't twist the dough into any new shapes as it will strain their "
                "'growth' during the frying process.\n6. Making this is a labor of love. But it's worth it.",
                "steps": "1. Using your electric mixer with the dough hook attachment, first mix the flour, egg, salt, baking powder, milk, and softened butter together on the lowest setting. Keeping the speed at stir, slowly add the water "
                "in a few separate batches. Knead the dough for 15 minutes. The dough should feel very soft, but should not stick to the bowl. Cover the dough, and let rest for 10 minutes. By the way, all of this can be done by hand if you don’t "
                "have a mixer. Just knead the dough for 5-10 minutes longer.\n2. On a clean, lightly floured surface, form the dough into a long flat loaf shape, about 1/4-inch thick and 4 inches wide. Take the time to make it truly uniform. Place "
                "it in the center of a large piece of plastic wrap on a baking sheet or long, flat plate, and wrap the dough, tucking the two ends of the plastic under the loaf, and ensuring that the dough is completely covered. Refrigerate overnight."
                "\n3. In the morning, take out the dough and let it sit on the counter (wrapped) for 1 – 2 hours until the dough is back to room temperature and VERY, VERY soft to the touch. This step is critical. If you don’t let the dough come back "
                "to room temperature, it won't fry up properly.\n4. Now prepare the oil for frying using your wok. You can also use a large pan with some depth for added safety. The goal is to have a large vessel, so that you can produce authentically "
                "long crullers. Use medium heat to slowly bring the oil up to 400 degrees.\n5. While the oil is heating up, you can unwrap the dough. Gently flip the dough onto a lightly floured surface, peeling off the plastic wrap. Very lightly flour "
                "the top side of the dough also. Next, cut the dough into 1-inch wide strips (try to cut an even number of strips).\n6.Then stack them two by two…And press the center, lengthwise, with a chopstick.Hold the two ends of each piece, and gently "
                "stretch the dough to a 9-inch long rope.\n7. Once the oil reaches 400 degrees, carefully lower the stretched dough into the oil. If the oil temperature is right, the dough should surface right away. Now take a long cooking tool (we used chopsticks, "
                "but you could also use tongs), and quickly roll the dough in a continuous motion for about a minute.\n8. You can fry one to two at a time. Just be sure to take the time to continuously roll the dough in the oil. The youtiao is done once they "
                "turn light golden brown. Try not to over-fry them as they become unpleasantly crunchy rather than chewy and delicious.\n9. Now, repeat those steps with the remaining you tiao dough. You might want two people manning the process—one to form and place "
                "the dough into the fryer and one to roll the dough around once it’s in the oil.\nEnjoy these!",
                "keywords": "vegetarian",
                "views": 8, "likes": 3, "image": "SoyMilkChineseFriedDough.jpg"},
                {"text": "breakfast", "recipe_name": "Taiwan Seafood Congee",
                "short_description": "Congee is probably the most common mainstay of the Chinese breakfast. It is a mild-flavored rice porridge that has been cooked for a long time with plenty of water to soften the rice. To give the congee some flavor, it is usually "
                "served with different toppings that vary by region. Here our toppings are a handful of dried scallop and a few pieces of shrimp.",
                "description": "Seafood congee has such a rich flavor that you can hardly imagine it contains just water, and no chicken stock.\n The star of this dish is dried scallop (conpoy).\nDried scallop is made from the adductor muscles of scallops.Pungent and "
                "compact, it has a highly concentrated flavor of the sea. Different from dried shrimp, conpoy is known for its sweet and delicate aroma.\nThere are two main types of conpoy: one made from river scallops and one made from sea scallops (also known as hotate "
                "in Japanese). We often use the river type, which has a milder and sweeter flavor. They won't be particularly overwhelming in a light dish like this congee.\nIt¡¯s quite magical, that you only need a few pieces of dried scallop to create a rich broth or "
                "sauce within minutes.\nDried scallop might not be a common ingredient in your pantry, but definitely grab it if you see it next time you're at an Asian market. It lasts up to a year in the fridge, and even longer in the freezer. Whenever you're out of "
                "stock or meat, just pop a few scallops into your soup. The rich flavor will surprise you!",
                "ingredients": "50 grams (1/2 cup) dried scallop\n100 grams (1/3 cup) rice\n100 grams (8 ¨C 10) shrimp\n1 teaspoon Shaoxing wine (or Japanese sake)\n1/2 teaspoon minced ginger\n3/8 teaspoon salt, or to taste\n1/2 teaspoon sesame oil\n2 tablespoons chopped green onion (green part)",
                "steps": "1. Rinse dried scallop. Place in a small bowl and tap water to cover. Let rehydrate for 2 to 3 hours.\n2. Rinse rice a few times and transfer to a large pot. Add 2 liters (8 cups) water. Bring to a boil over high heat. Stir a few times. Turn to "
                "medium low or medium heat. Cover the pot halfway to keep the water boiling without spilling. Cook for 30 minutes. Stir the congee a few times during cooking.\n3. Cut the shrimp down the center of the back into two thin pieces.\n4. Combine shrimp, Shaoxing "
                "wine, 1/2 teaspoon ginger, and 1/8 teaspoon salt in a small bowl. Mix well and set aside.\n5. Drain dried scallop. Tear into smaller pieces by hand. Set aside.\n6. When the congee has been cooking for 30 minutes and starts to thicken, add dried scallop. Keep "
                "cooking with the pot half covered, until the congee achieves the desired thickness, 15 to 20 minutes. Be careful, the congee will get quite thick and sticky towards the end. Stand close to the pot and stir frequently. It will easily spill if covered too much "
                "or if the heat is too high. The rice will stick to the bottom if you don't stir enough.\n7. When the congee is cooked, add shrimp and the remaining 1/4 teaspoon ginger. Stir a few times. Stop heat immediately. Add the remaining 1/4 teaspoon salt or salt to taste. "
                "Stir well. Drizzle with sesame oil and scatter with green onion.\n8. Serve warm.\nThe nutrition facts are calculated based on 1 of the 4 servings generated by this recipe.",
                "keywords": "meat, fish, seafood",
                "views": 17, "likes": 10, "image": "TaiwanSeafoodCongee.jpg"},
                {"text": "breakfast", "recipe_name": "Thai Bananna Pancakes",
                "short_description": "Most people know roti as an Indian savoury flatbread to mop up curries, but in Thailand it is often served as a sweet pastry. They are irresistible, especially when stuffed with banana and served with a good drizzle of sweetened condensed milk and a sprinkling of sugar.",
                "description": "Thai roti is one of THE most popular snacks/desserts amongst visitors to Thailand! It can also served as breakfast.You can see roti carts at many tourist attractions around the country, and nowadays, vendors offer so many different filling options like bananas, "
                "chocolate sauce, nutella, apples, etc. which, by the way, were not available when I was a kid, so roti has come a long way! If you go to non-touristy parts of Thailand you may still see some old-school roti vendors that still don’t offer many fancy fillings.\nNo one will ever "
                "say roti is good for you, but by making it at home, you can make it a little less bad! Street vendor rotis are tasty, but they don’t usually use the best of ingredients. You’ll notice that many vendors use what looks like butter, but it’s really margarine which is full of trans "
                "fat and is really bad for your health. They also most likely use the cheapest vegetable oil they can get a hold of, which is also not the best for you. This is not true of some fancier roti places, by the way, but it is true of most street carts. So at home, you can use real butter, "
                "and for the cooking you could use avocado oil which is a healthy, heat resistant, neutral flavoured cooking oil.",
                "ingredients": "1 ½ tsp salt\n1 Tbsp sweetened condensed milk (or sub 1 Tbsp sugar)\n1 egg, large\n260 ml water\n500 g all-purpose flour\n55 g unsalted butter, room temp\n1½ Tbsp unsalted butter (for coating the dough)\n1 Tbsp neutral flavoured (for coating the dough)\nNeutral flavoured oil for cooking"
                "Extra unsalted butter for cooking (optional)\nFillings & Toppings (just some ideas, you can put whatever you want in it!):\nBanana (choose ones with just a tiny hint of green on the skin, but not so green that it tastes bad! Too-ripe bananas will turn mushy quickly when cooked)\n"
                "Sweetened condensed milk\nNutella or chocolate sauce\nGranulated sugar\nTools:\nFlat, thick-bottomed frying pan, 12-inches in diameter (or bigger is better if you have one)",
                "steps": "To make the dough:\n1. In a large mixing bowl, combine salt and water and whisk until salt is dissolved. Add condensed milk and egg, whisk until combined.\n2. In another bowl, add flour and butter, and use your fingers to rub butter it into flour until no more big chunks are visible."
                "3. Add flour-butter mixture to water mixture and knead with your hands quickly just until all the dry flour has been absorbed. It’ll looks like a really shaggy, rough dough. Cover bowl with a damp cloth or plastic wrap and let rest for 15 – 30 minutes. (This resting step, called autolyse, is optional, "
                "but it will allow water to absorb into the flour and will reduce the total kneading time you need over all.)\n4. Once dough has rested, transfer onto a clean work surface and continue kneading with your hands for about 5 minutes. It will feel too moist at first, but it should feel drier after a few minutes. "
                "If after a few minutes of kneading the dough is still sticking to your hands, add a little bit of extra flour and knead it in. When you're done kneading, the dough won't be super smooth. In fact, the dough may seem a little bit rough on the surface; this is okay as long as the texture and moistness of the dough "
                "is even all throughout. The dough should be quite moist and may feel tacky, but it shouldn’t stick to your hands.\n5. Once the dough is kneaded, let rest for another 10-15 minutes to relax the gluten. This step is also optional, but it will make it easier for you to separate the dough into portions."
                "6. While dough is resting, mix together melted butter and oil for coating dough balls.\n7. Stretch dough into a log, then cut into 80g pieces (you will get about 11 pieces total). Note: 80g dough balls is for roti made in a 12-inch pan.\n8. Form each dough piece into a ball by pinching the edges together towards "
                "the centre (see video for technique). Doesn’t have to be perfect, but you want it to be round.\n9. Brush the butter/oil mixture on the bottom of the container you’re using to store dough balls. Then brush each dough ball generously with butter mixture and place into container.\n10.Let dough rest at least 3 hours, "
                "or you can refrigerate the dough and cook it the next day. If dough is refrigerated, remove from fridge at least 2 hours before using so it can come to room temp.\nEasy way to shape the roti:\n1. On a clean, lightly oiled work surface, press a dough ball into a flat disk.\n2. Grab the edge, one section at a time, "
                "and stretch it out as far as it will go without tearing. Press the edge onto the counter so it doesn’t shrink back.\n3. Go around the piece stretching until you have a very thin sheet of dough.\n4. Use a knife to trim off the very edge of the dough which tends to be thicker.\nTo cook the roti:\n1. Heat a 12-inch "
                "flat skillet (or bigger) over medium heat and add enough oil to coat the bottom. Be on the generous side with oil or you will not get a nice crisp roti. Add a little piece of dough scrap into the pan as a heat tester, and once it’s bubbling in the oil, you’re ready to cook the dough.\n2. Carefully transfer the "
                "stretched dough into the pan, trying not to let it fold onto itself during the transfer. Once you’ve placed the dough, quickly use a spatula to straighten out any edges that have folded.\n3. Arrange banana (or whatever filling you’re using) in the centre of the dough in a square, about 12-16 slices. Make sure you "
                "don’t put too much or you won’t be able to cover it with the dough. Quickly fold the edges of the roti over the banana; don’t wait to long before folding or the dough will become stiff and hard to fold.\n4. Once the bottom side has browned slightly, flip and brown the other side. Keep flipping it back and forth about "
                "every minute or so until both sides are well browned and crispy. Total cooking time should be about 4-5 minutes.\n5. If you wish, and add a little piece of butter beside the roti, then move the roti to coat it in this melted butter. Let it cook in this butter for about 30 seconds.\n6. Transfer roti onto a cutting board "
                "and cut into 12-16 pieces.\n7. Use a bench scraper to place it onto a serving plate. Let it cool off a bit before eating cuz that banana is HOT!\n8. When ready to eat, drizzle condensed milk (or chocolate sauce) and sprinkle on some granulated sugar. Enjoy!",
                "keywords": "vegetarian, healthy",
                "views": 20, "likes": 13, "image": "ThaiBananaPancakes.jpg"} ]
        
        oceania_recipes = [
                {"text": "breakfast", "recipe_name": "Vegemite on Toast",
                "short_description": "No Aussie breakfast is complete without vegemite…that ubiquitous yeast mix that the rest of the world loves to hate. It is ours and ours alone. Spread onto a slice of hot toast, it is Australian all the way!",
                "description": "Vegemite is a yeast extract obtained from the leftovers after brewing beer. It is essentially the same product as Marmite, but many people argue about which is better. For all intents and purposes, they are pretty similar in substance. While Australians will seriously caution against ever eating Vegemite on "
                "its own, they will equally encourage how delicious it is when used properly. By learning the proper proportional use and what dishes are enhanced with Vegemite, you can learn to enjoy just as much as any Aussie.  If you often eat toast for breakfast but you get tired of the blandness of butter alone, or you want a salty "
                "alternative to jam, Vegemite is a great alternative. It complements the blandness of butter very well while adding a rich, salty taste. ",
                "ingredients": "Vegemite\nbread,\nbutter",
                "steps": "1. Toast bread.\n2. Spead butter.\n3. Spread vegemite sparingly",
                "keywords": "vegetarian",
                "views": 18, "likes": 16, "image": "Vegemite.jpg"},
                {"text": "breakfast", "recipe_name": "Ricotta Hotcakes with Honeycomb Butter",
                "short_description": "Super, super tender and moist hotcakes that are sugar free and perfect for breakfast or brunch",
                "description": "Unlike regular pancake batters where flour forms the bulk, these hotcakes get their body from ricotta and whipped egg whites. It keeps them sublimely light and tender but as I also said this morning whilst digging into a thick stack “They’re hella filling” (it’s all that protein!). I adapted the recipe a tiny "
                "bit, using less ricotta than stated (just cos 1 1/2 tubs seemed excessive to me) and also by only partially mixing it in. That way you get little nuggets of creamy ricotta every so often. Turns out my suspicions were right about the honeycomb butter, it’s literally crushed honeycomb candy mixed with unsalted butter. For the "
                "sake of convenience I bought a Crunchie bar, cut off the chocolate coating and used the honeycomb from that. It may not seem like this butter is necessary (I probably would have skipped past it had I not tried it at the restaurant) but I adore it here, adding a dulcet hint of vanilla to each bite. Recipe adapted slightly from "
                "Bill Granger’s recipe",
                "ingredients": "For the Honeycomb butter\nOne 40 g Crunchie bar, (or 20 g /~1 oz of honeycomb candy)\n50 g unsalted butter\n1 tsp honey\nFor the hotcake batter:\n4 eggs, separated\n3/4 cup (185 ml) milk, any kind\n1 cup (125 g) plain flour\n1 heaped tsp baking powder\n1/4 tsp salt\n1 1/3 cups (300 g/10.7 oz) ricotta",
                "steps": "To make the honeycomb butter:\nCut the Crunchie bar into chunks and then use a sharp knife to slice off the outer layer of chocolate (you only want the middle honeycomb part). Place the honeycomb into a sandwich bag and bash with a rolling pin so that it's the texture of coarse breadcrumbs. Pour into a bowl along with "
                "the butter and honey. Cream together until well mixed then form into a log and wrap in clingfilm (or form individual scoops using a small, mechanical ice cream scoop). Chill until needed.\nTo make the hotcakes:\nIn a large jug, stir together the egg yolks, milk, flour, baking powder and salt with a fork. Add the ricotta to the "
                "jug and mix just a little (seriously like 3 stirs; you want tasty ricotta lumps). In a large bowl, whisk the egg whites until stiff. Pour the contents of the jug into the large bowl and fold in using a rubber spatula. There should be some lumps of ricotta throughout. Heat a large frying pan over a medium heat with enough vegetable "
                "oil to coat the pan. Scoop about 1/3 cup of batter into the pan to make 1 hotcake (depending on the size of your pan you can cook around 2 or 3 at a time). Use a metal spatula to check when the underside of the hotcake is golden, then flip and cook on the other side until golden as well. Remove to a plate and serve warm with the "
                "honeycomb butter, maple syrup and fresh fruit.",
                "keywords": "vegetarian",
                "views": 13, "likes": 10, "image": "RicottaHotcakes.jpg"},
                {"text": "breakfast", "recipe_name": "Corn Fritters with Avocardo Salsa",
                "short_description": "Not just another corn fritter – these are Bill Granger’s famous corn fritters! This really is restaurant quality food made in your own home. The flavour will knock your socks off!",
                "description": "These are the legendary Bill Granger Corn Fritters with Avocado Salsa. The extra step that makes these corn fritters really special is blending some of the corn and cilantro (coriander) into the batter - it makes the whole fritter truly taste of corn, rather than just bursts of it when you bite into kernels. This recipe "
                "makes 12 fritters and serves 4.",
                "ingredients": "3 cups (525g / 18oz) fresh corn kernels (~ 3 large corn cobs)\n1 small red onion chopped\n2 Eggs\n1/4 cup cilantro/coriander leaves and some stems (lightly packed)\n1 tsp sea salt\nFreshly ground Black pepper\n1 cup plain flour\n1 tsp baking powder\n3 tbsp olive oil\nAvocado Salsa:\n1 large (or 2 small) ripe avocado, stone "
                "removed and diced\n1 1/2 tomatoes , seeded and diced (about 3/4 cup, diced)\n2 tbsp coriander/cilantro , roughly chopped\n2 tbsp lemon or lime juice\n2 tbsp finely chopped spring onions scallions or red onion\n1 dash Tabasco sauce , optional\n1/2 tsp sea salt\nFreshly ground Black pepper",
                "steps": "1. Turn on the oven to very low - just to keep the fritters warm.\n2. Place 2 cups of the corn kernels and the onion, eggs, coriander, salt and pepper in a bowl and whizz with a stick blender until most of the corn is pureed (but still lumpy, not completely smooth). You can also do this step in a blender or food processor.\n3. Stir "
                "through remaining corn, flour and baking powder until just combined.\n4. Heat 1 tablespoon of the oil in a skillet/fry pan over a medium high heat.\n5. When the oil is hot, drop 2 heaped tablespoons of mixture per fritter into the pan and cook in batches for 1 1/2 minutes each side, or until golden.\n6. Transfer to a baking tray and keep "
                "warm in the oven while you are making the rest of the fritters.\n7.To serve, stack 3 corn fritters on each plate and top with avocado salsa and extra cilantro/coriander leaves if desired.\nAvocado Salsa:\nCombine all ingredients, toss very gently.\nRecipe Notes:\n1. Fresh corn is best but you can use defrosted frozen or well drained canned "
                "corn kernels.\n2. Recipe very slightly adapted from this one by Bill Granger. The change I made was to stir through the flour after pureeing the corn because otherwise, there is a risk of over beating the flour which will make the fritters tough.",
                "keywords": "vegetarian, healthy",
                "views": 4, "likes": 4, "image": "CornFritters.jpg"}, ]

        Continents = {"North America": {"recipes": north_america_recipes},
                        "Latin America": {"recipes": latin_america_recipes},
                        "Africa": {"recipes": africa_recipes},
                        "Europe": {"recipes": europe_recipes},
                        "Asia": {"recipes": asia_recipes},
                        "Oceania": {"recipes": oceania_recipes}} 

        for cont, cont_data in Continents.items():
                c = add_continent(cont)
                for r in cont_data["recipes"]:
                        add_recipe(r["recipe_name"], c, r["short_description"], r["description"], r["ingredients"], r["steps"], r["keywords"], r["views"], r["likes"], r["image"])

        for cont in Continent.objects.all():
                for r in Recipe.objects.filter(continent=cont):
                      print("- {0} - {1}".format(str(cont), str(r)))    

def add_continent(name, views=0):
        c = Continent.objects.get_or_create(name=name)[0]
        c.views = views
        c.save()
        return c

def add_recipe(recipe_name, continent, short_description, description, ingredients, steps, keywords, views, likes, image):
        r = Recipe.objects.get_or_create(recipe_name=recipe_name, continent=continent)[0]
        r.short_description = short_description
        r.description = description
        r.ingredients = ingredients
        r.steps = steps
        r.keywords = keywords
        r.views = views
        r.likes = likes
        r.image = image
        r.save()
        return r

if __name__=='__main__':
        print("Starting breakfast population script...")
populate()

        
