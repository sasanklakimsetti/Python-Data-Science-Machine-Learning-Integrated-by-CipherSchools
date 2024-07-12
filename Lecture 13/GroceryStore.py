#Definition: This example combines variables. data types, conditionals, and loops to manage a grocery store inventory.
#Use Case in Real Life: A grocery store needs to keep track of its inventory. update it based on sales and restocks. and check the status of items.

store_name="Green Grocery"
inventory={
    "apples":50,
    "bananas":30,
    "cherries":20
}

def check_inventory(item):
    if inventory[item]>0:
        return f"{item.capitalize()} are in stock: {inventory[item]}"
    else:
        return f"{item.capitalize()} are out of stock"

def update_inventory(item,quantity):
    if item in inventory:
        inventory[item]+=quantity
    else:
        inventory[item]=quantity

print(check_inventory("apples"))
update_inventory("apples",-10)
print(check_inventory("apples"))
update_inventory("apples",40)
print(check_inventory("apples"))
update_inventory("oranges",100)
print(check_inventory("oranges"))
print(inventory)