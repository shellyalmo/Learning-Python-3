"""In this project, the purpose is to invite gamers to a game night, by automating the game night selector to get the most people.
"""

#Creating an empty list called gamers. This will be the list of people who are attending game night.

gamers = []

"""This function updates this list and adds a new gamer to the gamers list. Each gamer is a dictionary with the following keys:
"name": a string that contains the gamer's full or presumed name. E.g., "Vicky Very"
"availability": a list of strings containing the names of the days of the week that the gamer is available.
E.g., ["Monday", "Thursday", "Sunday"]
"""

def add_gamer(gamer,gamers_list):
    if "name" in gamer.keys() and "availability" in gamer.keys():
        gamers_list.append(gamer)
    
            
#Adding the first gamer. Her name is Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays.
kimberly = {"name":"Kimberly Warner", "availability":["Monday","Tuesday","Friday"]}
add_gamer(kimberly,gamers)

#Adding more gamers
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

"""calculating which nights would have the most participation, by creating a frequency table which correlates each day of the week 
with gamer availability.
This function called build_daily_frequency_table returns a dictionary with the days of the week as keys 
and 0s for values. We'll be using this to count the availability per night. """

def build_daily_frequency_table():
    frequency_table = {
    "Monday" : 0,
    "Tuesday" : 0,
    "Wednesday" : 0,
    "Thursday" : 0,
    "Friday" : 0,
    "Saturday" : 0,
    "Sunday" : 0
    }
    return frequency_table


count_availability = build_daily_frequency_table()

"""This funtionc called calculate_availability iterates through each gamer and through each day in the gamer's availability. 
For each day in the gamer's availability, it adds one to that date on the frequency table."""

def calculate_availability(gamers_list,available_frequency):
    for gamer_key in gamers_list:
        for day in gamer_key["availability"]:
            available_frequency[day] += 1
    
    
#finding the best night to run the game Abruptly Goblins.

calculate_availability(gamers,count_availability)
print(count_availability)

#picking the day with the most available people to attend.
#This function takes a dictionary availability_table and returns the key with the highest number.

def find_best_night(availability_table):
    biggest_value = float("-inf")
    key_of_biggest_value = ""
    for key,value in availability_table.items():
        if value > biggest_value:
            biggest_value = value
            key_of_biggest_value = key
    return key_of_biggest_value


game_night = find_best_night(count_availability)
print(game_night)

#This function returns a list of people who are available on that particular day.
def available_on_night(gamers_list,day):
    people_available_that_day = []
    for gamer in gamers_list:
        for value in gamer["availability"]:
            if value == day:
                people_available_that_day.append(gamer)
    return people_available_that_day
attending_game_night = available_on_night(gamers,game_night)
print(attending_game_night)

#creating a form email to send to each of the participants.
form_email = "Hello {}! You are invited to play {} on {} night. See you there!"

def send_email(gamers_who_can_attend,day,game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(gamer['name'], game, day))
send_email(attending_game_night,game_night,"Abruptly Goblins!")
    
#Creating a second game night of the week.
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]
second_night_availability = build_daily_frequency_table()
second_night = find_best_night(second_night_availability)
print(second_night)

#Sending another email about the second game night
available_second_game_night = available_on_night(gamers,second_night)
send_email(available_second_game_night,second_night,"Abruptly Goblins!")
