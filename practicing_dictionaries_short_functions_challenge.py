"""This program helps me review Python functions by providing some challenge exercises involving dictionaries."""

# This function takes a dictionary named as a parameter, and returns the sum of the values of the dictionary.
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total
# tests:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# This function takes a dictionary, with all integer keys and values, as a parameter, and returns the sum of the values of all even keys.
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary.get(key)
  return total
# tests
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# This function takes a dictionary with integer values, and adds 10 to every value inthe dictionary and returns it.
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
# tests:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# This function takes a dictionary, and returns a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  new_list = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        new_list.append(value)
  return new_list
    
# tests
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# This function takes a dictionary, and returns the key associated with the largest value in the dictionary.
def max_key(my_dictionary):
  biggest_value = float("-inf")
  key_of_biggest_value = ""
  for key,value in my_dictionary.items():
    if value > biggest_value:
      biggest_value = value
      key_of_biggest_value = key
  return key_of_biggest_value

#tests
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# This function takes a list of strings, and returns a dictionary of key/value pairs where every key is a word and every value is the length of that word.
def word_length_dictionary(words):
  list_of_keys = []
  list_of_values = []
  for key_name in words:
    list_of_keys.append(key_name)
    list_of_values.append(len(key_name))
  new_dictionary = {key:value for key,value in zip(list_of_keys,list_of_values)}
  return new_dictionary
  
# tests
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# This function takes a list of elements, and returns a dictionary containing the frequency of each element.
def frequency_dictionary(words):
  list_of_keys = []
  list_of_values = []
  for key_name in words:
    list_of_keys.append(key_name)
    list_of_values.append(words.count(key_name))
  return {key:value for key, value in zip(list_of_keys,list_of_values)}

# tests
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# This function takes a dictionary, and returns the number of unique values in the dictionary.
def unique_values(my_dictionary):
  list_of_values = []
  for value in my_dictionary.values():
    list_of_values.append(value)
  count = 0
  for value_item in list_of_values:
    if list_of_values.count(value_item) > 1:
      count += 1
      list_of_values.remove(value_item)
  if all(value_item == list_of_values[0] for value_item in list_of_values):
      count = 1
  #print(list_of_values)
  return count

# tests
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# # This function takes a dictionary where the key is a last name and the value is a list of first names. The function returns a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
def count_first_letter(names):
  letters = {}
  for key in names.keys():
    if key[0] not in letters:
      letters.update({key[0]:len(names[key])})
    else:
      letters[key[0]] += len(names[key])
   return letters
 
# tests
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
