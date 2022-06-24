def get_pet_shop_name(pet_name):
    return pet_name["name"]

def get_total_cash(admin_cash):
    return admin_cash["admin"]["total_cash"]
    
def add_or_remove_cash(admin_cash, money):
    admin_cash["admin"]["total_cash"] += money
    
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]
    
def increase_pets_sold(more_pets, sold):
    more_pets["admin"]["pets_sold"] += sold

def get_stock_count(pet_stock):
    return len(pet_stock["pets"])

def get_pets_by_breed(pets, breed):
    count = 0
    for type in pets:
        if pets["pets"]["breed"] == breed:
            count = count + 1
    return count


def get_pets_by_breed(pets, breed):
    count = 0
    for num_of in pets["pets"]["breed"]:
        if num_of == breed:
            count += 1
    return count

I can't hear anything from slack
Did you allow slacks to access microphont? or Audio