####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "CupK3K"
signature_flavors = ["lotus", "mahalbiya", "honeycrisp", "spicy chocolate"]
order_list = []


def print_menu():
    for item in menu:
        print (item)
   

def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for type in original_flavors:
        print (type)
   

def print_signatures():
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for type in signature_flavors:
       print (type)
    

def is_valid_order(order):
    if (order.lower() in menu or order.lower() in original_flavors or order.lower() in signature_flavors):
        return True
    else:
        return False

def get_order():
    while True:
        orderInput = input("What is your order? ")
        if (is_valid_order(orderInput)):
            order_list.append(orderInput)
            print ("Your Order is: %s" %order_list) 
        elif (orderInput.lower() == "exit"):
           
            return order_list
        else:
            print ("Please type an existing item or type exit to finish ordering")

def accept_credit_card(total):
    if (total >= 5):
        return "You may pay Cash or KNET"
    else:
        return "Please pay in Cash"

    

def get_total_price(order_list):
    total = 0
    for item in order_list:
        if (item in menu):
            total += menu[item]
        elif (item in original_flavors):
            total += original_price
        elif (item in signature_flavors):
            total += signature_price
    
    return total


def print_order(order_list):
    print()
    print("Your order is: ")
    print(order_list)
    print("Your Total is: ")
    print("%s kd" %get_total_price(order_list))
    print(accept_credit_card(get_total_price(order_list)))

    
