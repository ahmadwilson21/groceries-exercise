# groceries.py

#from pprint import pprint
from decimal import Decimal
import operator 
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


print("--------------")
print("THERE ARE ", len(products), " PRODUCTS")
print("--------------")

length = len(products) #the number of products in the initial array

products.sort(key = operator.itemgetter("name")) # this sorts the list of products by name

for p in products: # iterates through each dictionary in the list
    name= p["name"]  # retrieves the name of each product
    price = float((p["price"])) 
    price= Decimal(price) # makes the price a decimal 
    price = round(price, 2) #rounds decimal to two places
    print(f"+ {(name)} (${price})") # prints the name & price in desired format
   



# TODO: write some Python code here to produce the desired output

# function that retrieves the department name from a dictionary
def department_name(department): 
    return department["department"]

department_list = sorted(products, key = department_name) #sorts the list by department name

new_list = [d["department"]for d in department_list] #makes a list of the department names
new_set = list(set(new_list)) #deletes duplicates from the list of department names

product_count = 0

department = ""

print("--------------")
print("THERE ARE ", len(new_set), " PRODUCTS")
print("--------------")

for d in department_list:
    #if department in new_list:
    #    product_count = product_count + 1
    #    duplicate = True
    
    if department != (d["department"].title()):
        
        
        department = d["department"] # assigns the deparmtent name to a variable
        product_count = new_list.count(department) #counts the number of times a dept name was repeated from earlier list
        department = d["department"].title() #Makes each word in string uppercase
      


        #Creates the statement saying the deparment name and product count preceded by plus sign
        statement = (f"+ {department} ({product_count}")
        if product_count >1:
            statement = (f"{statement} products)")
        else:
            statement = (f"{statement} product)")


        print(f"{statement}")

#-------------vbv cb                     -
#THERE ARE 20 PRODUCTS:
#--------------
# + All-Seasons Salt ($4.99)
# + Chocolate Fudge Layer Cake ($18.50)
# + Chocolate Sandwich Cookies ($3.50)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
# + Dry Nose Oil ($21.99)
# + Fresh Scent Dishwasher Cleaner ($4.99)
# + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
# + Green Chile Anytime Sauce ($7.99)
# + Light Strawberry Blueberry Yogurt ($6.50)
# + Mint Chocolate Flavored Syrup ($4.50)
# + Overnight Diapers Size 6 ($25.50)
# + Peach Mango Juice ($1.99)
# + Pizza For One Suprema Frozen Pizza ($12.50)
# + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# + Pure Coconut Water With Orange ($3.50)
# + Rendered Duck Fat ($9.99)
# + Robust Golden Unsweetened Oolong Tea ($2.49)
# + Saline Nasal Mist ($16.00)
# + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)

#--------------
#THERE ARE 10 DEPARTMENTS:
#--------------
# + Babies (1 product)
# + Beverages (5 products)
# + Dairy Eggs (1 product)
# + Dry Goods Pasta (1 product)
# + Frozen (4 products)
# + Household (1 product)
# + Meat Seafood (1 product)
# + Pantry (2 products)
# + Personal Care (2 products)
# + Snacks (2 products)
