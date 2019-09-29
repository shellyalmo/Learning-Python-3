#This program is creating receipts for customers of the fictional store called "Lovely Loveseat". In the program, the store's catalog is stored in variables, and the total price for each customer is calculated and printed.

#A furniture item description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
#The price
lovely_loveseat_price = 254.00

#A furniture item description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
#The price
stylish_settee_price = 180.50

#A furniture item description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
#The price
luxurious_lamp_price= 52.15

#The sales tax, because we are a real business
sales_tax = .088

#The customers
customer_one_total = 0
#The purchasing list of the customers
customer_one_itemization = ""

#The first customer is purchasing the loveseat and the lamp. 
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
#The total price also includes sales tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printing out the receipt
print ("Customer One Items:")
print (customer_one_itemization)

print("Customer One Total:")
print (customer_one_total)
