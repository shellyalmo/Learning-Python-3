"""This program is providing physics students functions that will help them calculate some fundamental physical properties."""

#The given data (global parameters)
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#This function is converting the temperature from Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9
  return c_temp

#testing f_to_c function
print ("100 degress Fahrenheit to Celsius is: " + str(f_to_c(100)))

#This function is converting the temperature from Celsius to Fahrenheit 
def c_to_f(c_temp):
  f_temp = c_temp*(9/5) + 32
  return f_temp

#testing c_to_f function
#c0_in_farenheit = c_to_f(0)
print("0 degress Celsius to Fahrenheit is: " + str(c_to_f(0)))

#This function is calculating the force by multiplying the mass by the acceleration
def get_force(mass,acceleration):
  return (mass*acceleration)

#testing get_force function with the given data
train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#This function is calculating the energy by multiplying the mass by C squared. The constant C is the speed of light (3x10^8 m/s)
def get_energy(mass,c = 3*10**8):
  return (mass*(c**2))
  
#testing get_energy function
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#This function is calculating the work by multiplying the force by the distance
def get_work(mass,acceleration,distance):
  return ((get_force(mass,acceleration))*distance)

#test get_work function
train_work = get_work(train_mass,train_acceleration,train_distance)
print ("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
