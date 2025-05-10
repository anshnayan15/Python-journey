items = {
    'red leather ball': 400,
    'white leather ball': 600,
    'english willow bat': 15000,
    'kashmir willow bat': 5000,
    'pair of batting gloves': 1200,
    'pair of wicket keeping gloves': 2500,
    'cricket helmet': 3500,
    'leg pads': 3000,
    'thigh guard': 800,
    'cricket kit bag': 4000
}

print("welcome to bowled by stats cricket store")

print("red leather ball : Rs 400")
print("white leather ball : Rs 600")
print("english willow bat : Rs 15000")
print("kashmir willow bat : Rs 5000")
print("pair of batting gloves : Rs 1200")
print("pair of wicket keeping gloves : Rs 2500")
print("cricket helmet : Rs 3500")
print("leg pads : Rs 3000")
print("thigh guard : Rs 800")
print("cricket kit bag : Rs 4000")

order_total = 0

item_1 = input("what do you want = ")
if item_1  in items:
    order_total += items[item_1]
    print(f"your {item_1} is headed for checkout")
else:
    print(f"your order {item_1} is unavaiable")
    
another_order= input("need anything else(Yes/No?")

if another_order == "Yes":
   item_2 = input("name of the second item?")
   if item_2 in items:
       order_total += items[item_2]
       print(f"your item {item_2} has been added too")
   else:
       print(f"sorry {item_2} is not available")
else:
    print("Okay, no more items added.")


print(f"you have to pay {order_total} rupees")
