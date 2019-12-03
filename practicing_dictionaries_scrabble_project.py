"""This project is processing data from a scrabble game. It uses dictionaries to organize players, words and points."""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combining the lists of letters and points into one dictionary maps a letter to its point value.
letter_to_points = {key:value for key,value in zip(letters,points)}
# Taking in account blank tiles
letter_to_points.update({" " : 0})

#A function that takes a word and returns how many points that word is worth.
def score_word(word):
  total_points = 0
  for letter in word:
    total_points += letter_to_points.get(letter,0)
  return total_points

# test: should return 15:
# print(score_word("BROWNIE"))

# The data of the game: a dictionary that maps players to a list of the words they have played.
player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
    

# This function contains the mapping of players to how many points they've scored.
def update_point_totals(dictionary_of_player_to_words,player_name):
  player_to_points = {}
  words = dictionary_of_player_to_words.get(player_name)
  player = player_name
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
  return player_to_points

# This function takes in a player and a word, and adds that word to the list of words they’ve played.
# Then it calls the previous function to check how many points the player has earned.
def play_word(player,word):
  upper_word = word.upper()
  for player_name in player_to_words.keys():
    if player == player_name:
      player_to_words[player].append(upper_word)
  
  return update_point_totals(player_to_words,player)
print(letter_to_points)

# test: should return {'player1: 45'}
# print(play_word("player1","bunny"))

