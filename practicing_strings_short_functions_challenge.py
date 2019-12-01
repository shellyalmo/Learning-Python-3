"""This program is a series of short function challenges for practicing strings."""


# This function returns the total number of unique letters in the string. Uppercase and lowercase letters are counted as different letters.
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count

# tests
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# This function takes a strung and a character as arguments, and returns the number of times the character appears in the string.
def count_char_x(word,x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count
  
# tests
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# This function takes two strings as arguments,and returns the number of times the first appears in the second.
def count_multi_char_x(word,x):
  splitted=word.split(x)
  joined = "".join(splitted)
  print(splitted)
  print(joined)
  lenJoined = len(joined)
  print(lenJoined)
  lenWord = len(word)
  emptylen = lenWord - lenJoined
  print(emptylen)
  uniquelen = emptylen/(len(x))
  print(uniquelen)
  return uniquelen

# tests
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# This function takes a string and two characters as arguments, which mark the beginning and the end of a string. The function returns the substring between the first occurrence of the beginning and the end.
def substring_between_letters(word,start,end):
  if (start and end) in word:
    new_word = word[word.find(start)+1:word.find(end)]
    return new_word
  else:
    return word
    
# tests
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
print(substring_between_letters("unicorn", "n", "r"))
# should print "ico"

# This function takes a string and an integer as arguments, and returns True if every word in the string has a length greater or equal to the int.
def x_length_words(sentence,x):
  every_word = sentence.split()
  for word in every_word:
    if len(word) < x:
      return False
    else:
      return True
    
# tests
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
print(x_length_words("we are the champions now", 2))
# should print true

# This function check if a name is in a string. It will return True if the name appears in the string in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters.
def check_for_name(sentence,name):
  if name.lower() in sentence or name.upper() in sentence or name.title() in sentence or name.swapcase() in sentence:
    return True
  else:
    return False

# tests
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
print(check_for_name("My name is Raja","rajA"))
# should print True

# This function takes a string and returns a string containing every other letter.
def every_other_letter(word):
  returned_string = ""
  for i in range(0,len(word),2):
    returned_string = "{}{}".format(returned_string, word[i])
    
  return returned_string
    
# tests
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter("?@#3"))
# should print ?# 

# This function gets a string and returns it reversed.
def reverse_string(word):
  returned_string = ""
  for i in range (len(word)-1,-1,-1):
    returned_string = "{}{}".format(returned_string,word[i])
    #easy solotuin is to do: return word[::-1]
  return returned_string

# tests
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# This function takes two words, finds the first letter of each word, and switches them.
def make_spoonerism(word1,word2):
  switched1 = word1.replace(word1[0],word2[0])
  switched2 = word2.replace(word2[0],word1[0])
  return "{} {}".format(switched1,switched2)

# tests
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# This function gets a word, and adds exclamation markss to the word until it's 20 characters long.
# If the word is already at least 20 characters long, the function returns word.
def add_exclamation(word):
  if len(word) < 20:
    while len(word) < 20:
      word += "!"
    return word
  else:
    return word

# tests
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
