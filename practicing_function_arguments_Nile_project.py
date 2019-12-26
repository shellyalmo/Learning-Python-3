"""In this project I'm manipulating arguments to help automate practices for a delivery company. 
I'm practicing using positional arguments, keyword arguments, default arguments, unpacking and more."""

from practicing_function_arguments_Nileproject_Nilefile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# This function is calculating the costs, with a default argument for shipping_type
def calculate_shipping_cost(from_coords,to_coords,shipping_type='Overnight'):
  #unpacking the tuples
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  #one way to calculate the distance:
  # distance = get_distance(from_lat,from_long,to_lat,to_long)
  #another way to calculate the distance:
  distance = get_distance(*from_coords,*to_coords)
  #fetching the key passed in the dictionary
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  #returning the formatted price
  return format_price(price)

# Test the function by calling: 
test_function(calculate_shipping_cost)

# This function calculates the drivers cost
def calculate_driver_cost(distance,*drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    #checking if the current driver is the cheapest one
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    #checking if the cheapest driver is the one stored in cheapest_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver
  
# Test the function by calling 
test_function(calculate_driver_cost)

# This function claculates the amount of money made, with keyword arguments passed into it.
def calculate_money_made(**trips):
  total_money_made = 0
  #iterating through the dictionary
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made += trip_revenue
  return total_money_made

# Test the function by calling 
test_function(calculate_money_made)
