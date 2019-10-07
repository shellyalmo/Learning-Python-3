"""This program takes the weight of a package and determines the cheapest way to ship that package. """
#cost of ground shipping by weight
def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
  elif weight >2 and weight <= 6:
    cost = weight * 3 + 20.00
  elif weight > 6 and weight <= 10:
    cost = weight * 4 + 20.00
  elif weight > 10:
    cost = weight * 4.75 + 20.00
  return cost

# test: print (ground_shipping())
# for 8.4 should return 53.6

# cost of premium ground shipping (does not change with the weight of the package.)
cost_premium_ground_shipping = 125

# cost of drone shipping
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 + 0.00
  elif weight >2 and weight <= 6:
    cost = weight * 9.00 + 0.00
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00 + 0.00
  elif weight > 10:
    cost = weight * 14.25 + 0.00
  return cost

 #test: print (drone_shipping())
# for 1.5 should return 6.75

# This function determines which method is cheapest and tells the user what is the price.
def cheapest_method(weight):
  if ground_shipping(weight) < cost_premium_ground_shipping and ground_shipping(weight) < drone_shipping(weight):
    print ("The cheapest shipping method is ground shipping.")
    print ("The cost of shipping a package that weighs " + str(weight) + " pounds is " + str(ground_shipping(weight)) + " dollars.")
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < cost_premium_ground_shipping:
    print ("The cheapest shipping method is drone shipping.")
    print ("The cost of shipping a package that weighs " + str(weight) + " pounds is " + str(drone_shipping(weight)) + " dollars.")
  elif cost_premium_ground_shipping < ground_shipping(weight) and cost_premium_ground_shipping < drone_shipping(weight):
    print ("The cheapest shipping method is premium ground shipping.")
    print ("The cost of shipping a package that weighs " + str(weight) + " pounds is " + str(cost_premium_ground_shipping) + " dollars.")
      
#tests
cheapest_method(4.8)
# this test should return 34.4
cheapest_method(41.5)
#this test should return 125
