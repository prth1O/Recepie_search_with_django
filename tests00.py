from py_edamam import Edamam
import pprint as pp
e = Edamam(nutrition_appid='33e2b843',
           nutrition_appkey='19cabd42f85ab1dd7a2c5075f2148bf7',
           recipes_appid='d2b39e3b',
           recipes_appkey='003a3b450bee5ae5c3977c81be5423bf',
           food_appid='b9689b5b',
           food_appkey='d7d6a5e7d612f7d7395df93d82008e79')
           
pp.pprint(e.search_nutrient("1 large apple"))
print()
pp.pprint(e.search_recipe("onion and chicken"))
print()
pp.pprint(e.search_food("coke"))
