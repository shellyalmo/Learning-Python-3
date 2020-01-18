# These are the emails I'm censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


#this function deals with punctuation in the string
def fix_punctuation(word):
    punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]
    for char in punctuation:
        word = word.strip(char)
    return word 

#this function is censoring a word from a string
def remove_from_text(some_string, word_or_phrase):
    censored_string = some_string
    number_of_stars = ""
    for i in range(0, len(word_or_phrase)):
        number_of_stars += "*"
    if word_or_phrase in some_string:
        censored_string = some_string.replace(
            " " + word_or_phrase, " " + number_of_stars)
    if word_or_phrase.title() in some_string:
        censored_string = censored_string.replace(
            word_or_phrase.title(), " " + number_of_stars)
    if fix_punctuation(word_or_phrase) in some_string:
        censored_string = censored_string.replace(
            fix_punctuation(word_or_phrase), " " + number_of_stars)
    return censored_string


# these words need to be censored
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "herself", "her"]

#this function removes a specific word from the proprietary_terms. Used for email two.
def remove_specific_from_text(some_string, list_of_specific_words):
    censored_string = some_string
    for word in list_of_specific_words:
        censored_string = remove_from_text(censored_string, word)
    return censored_string


negative_words = ["concerned", "behind", "dangerous", "danger", "alarming",     "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"]

# this function can censor any occurance of a word from the negative words list after any negative word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.
def remove_negative_and_specific(some_string, negative_words, list_of_specific_words):
    has_2_or_more_negative_words = False
    censored_string = some_string
    count_of_negative_words = 0
    positive_string = censored_string
    for word in censored_string.split():
        word = word.lower()
        word = fix_punctuation(word)
        if (word in negative_words):
            count_of_negative_words += 1
            if count_of_negative_words > 1:
                # positive_string = remove_from_text(positive_string, word)
                has_2_or_more_negative_words = True
    if has_2_or_more_negative_words == True:
        return remove_specific_from_text(positive_string, list_of_specific_words + negative_words)
    else:
        return remove_specific_from_text(positive_string, list_of_specific_words)


