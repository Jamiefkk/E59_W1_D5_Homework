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


# #issues
# def get_pets_by_breed(species, breed):
#     count = []
#     for pet in species:
#         if pet == breed:
#             count.append(pet["name"])
#     return count

# def find_pet_by_name(pet, name):
#     for pet_name in pet["pets"]["name"]:
#         if pet_name == name:
#             return pet_name

# something about this is wierd, we can sue this in our own but not here
# def get_pets_by_breed(pets, breed):
#     count = []
#     for pet in pets["pets"]["breed"]:
#         if pet == breed:
#             count.append(pet["name"])
#     return count

def get_pets_by_breed(pet_type, breed):
    count = []
    species = (pet_type["pets"])
    for pet in species:
        if pet ["breed"] == breed:
            count.append(pet["name"])
    return count

# def find_pet_by_name(pet_list, pet_name):
#     count = []
#     name = (pet_list["pets"])
#     for pet in name:
#         if pet ["name"] == pet_name:
#             count.append(pet["name"])
#     return count

def find_pet_by_name(pet_list, pet_name):
    count = None
    name = (pet_list["pets"])
    for pet in name:
        if pet ["name"] == pet_name:
            count = pet
    return count

def remove_pet_by_name(pet_list, pet_name):
    names = (pet_list["pets"])
    for name in names:
        if name == pet_name:
            names.pop(name)

def add_pet_to_stock(pet_list, new_pet):
    names = (pet_list["pets"])
    names.append(new_pet)

def get_customer_cash(customer_money):
        return customer_money ["cash"]

def remove_customer_cash(customer, money):
    customer ["cash"] -= money

def get_customer_pet_count(customer_number):
    count = 0
    for pet in customer_number["pets"]:
        count = count + 1
    return count
    
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    budget = get_customer_cash(customer)
    price = new_pet["price"]
    if price <= budget:
        return True
    else:
        return False

# def sell_pet_to_customer(self.cc_pet_shop, pet, customer):
