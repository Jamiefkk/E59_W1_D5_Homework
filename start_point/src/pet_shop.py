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

