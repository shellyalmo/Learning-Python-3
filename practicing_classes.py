"""This project implements the concepts of Object Oriented Programming by using Classes and Methods."""

class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "{name} is available from {start_time}:00 to {end_time}:00.".format(name=self.name, start_time=self.start_time, end_time=self.end_time)
  
  def calculate_bill(self,purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    return total_price
    
class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address is: {}".format(self.address)
  
  def available_menus(self,time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menu.append(menu)
    return str(available_menu)
  
class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

  
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch Menu', brunch_items, 11, 16)

early_bird_items = {
   'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird Menu', early_bird_items,15,18)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner Menu', dinner_items, 17,23)

kids_items = {
   'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids Menu', kids_items, 11, 21)

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('Arepas Menu', arepas_items, 10, 20)

flagship_store = Franchise('1232 West End Road',[brunch_menu,early_bird_menu,dinner_menu,kids_menu])
new_installment = Franchise('12 East Mulberry Street',[brunch_menu,early_bird_menu,dinner_menu,kids_menu])
arepas_place = Franchise('189 Fitzgerald Avenue',[arepas_menu])

first_business = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

second_business = Business("Take a' Arepa",arepas_place)

# print(brunch_menu.calculate_bill(['pancakes','home fries','coffee']))
# print(early_bird_menu)
# print(early_bird_menu.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

# print(flagship_store)
# print(flagship_store.available_menus(12))
# print(flagship_store.available_menus(17))
# print(arepas_place.available_menus(16))
