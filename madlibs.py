
import nltk


nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

from pattern.en import pluralize, conjugate

import random

from uncountable_nouns import uncountable_nouns
from idioms import idioms_dictionary
from gender_words import dictionary_gender


# Creating variables

  # """
  # Ask user for the input,
  # checks whether the input is legible
  # """
# adj1 = ''
# noun1 = ''
# verb1 = ''
# adj2 = ''
# noun2 = ''
# famous_person = ''
# verb2 = ''
# verb3 = ''
# noun3 = ''
# size_adjective1 = ''
# color_adjective1 = ''
# noun4 = ''
# noun5 = ''
# size_adjective2 = ''
# color_adjective2 = ''
# noun6 = ''
# noun7 = ''
# verb4 = ''

# while not (len(adj1) >= 2 and adj1.isalpha()):
#     adj1 = input('Type an adjective: ')
# while not (len(noun1) >= 2 and noun1.isalpha()):
#     noun1 = input('Type a noun (living thing): ')
# while not (len(verb1) >= 2 and verb1.isalpha()):
#     verb1 = input('Type a verb: ')
# while not (len(adj2) >= 2 and adj2.isalpha()):
#     adj2 = input('Type an adjective: ')
# while not (len(noun2) >= 2 and noun2.isalpha()):
#     noun2 = input('Type a noun: ')
# while not (len(famous_person) >= 2 and famous_person.isalpha()):
#     famous_person = input("Type a famous person: ")
# while not (len(verb2) >= 2 and verb2.isalpha()):
#     verb2 = input('Type a verb: ')
# while not (len(verb3) >= 2 and verb3.isalpha()):
#     verb3 = input('Type a verb: ')
# while not (len(noun3) >= 2 and noun3.isalpha()):
#     noun3 = input('Type a noun: ')
# while not (len(size_adjective1) >= 2 and size_adjective1.isalpha()):
#     size_adjective1 = input('Type a size adjective: ')
# while not (len(color_adjective1) >= 2 and color_adjective1.isalpha()):
#     color_adjective1 = input('Type a color adjective: ')
# while not (len(noun4) >= 2 and noun4.isalpha()):
#     noun4 = input('Type a noun: ')
# while not (len(noun5) >= 2 and noun5.isalpha()):
#     noun5 = input('Type a noun: ')
# while not (len(size_adjective2) >= 2 and size_adjective2.isalpha()):
#     size_adjective2 = input('Type a size adjective: ')
# while not (len(color_adjective2) >= 2 and color_adjective2.isalpha()):
#     color_adjective2 = input('Type a color adjective: ')
# while not (len(noun6) >= 2 and noun6.isalpha()):
#     noun6 = input('Type a noun: ')
# while not (len(noun7) >= 2 and noun7.isalpha()):
#     noun7 = input('Type a noun: ')
# while not (len(verb4) >= 2 and verb4.isalpha()):
#     verb4 = input('Type a verb: ')

# adj1 = input('Type an adjective: ')
# noun1 = input('Type a noun (living thing): ')
# verb1 = input('Type a verb: ')

# adj2 = input('Type an adjective: ')
# noun2 = input('Type a noun: ')
# famous_person = input("Type a famous person: ")
# verb2 = input('Type a verb: ')

# verb3 = input('Type a verb: ')
# noun3 = input('Type a noun: ')
# size_adjective1 = input('Type a size adjective: ')
# color_adjective1 = input('Type a color adjective: ')

# noun4 = input('Type a noun: ')
# noun5 = input('Type a noun: ')

# size_adjective2 = input('Type a size adjective: ')
# color_adjective2 = input('Type a color adjective: ')
# noun6 = input('Type a noun: ')

# noun7 = input('Type a noun (living thing): ')
# verb4 = input('Type a verb: ')


adj1 = 'easy-going'
noun1 = 'cat'
verb1 = 'show'
adj2 = 'furry'
noun2 = 'robot'
famous_person = 'bjorn'
verb2 = 'stop'
verb3 = 'cry'
noun3 = 'pill'
size_adjective1 = 'huge'
color_adjective1 = 'red'
noun4 = 'pill'
noun5 = 'bus'
size_adjective2 = 'tiny'
color_adjective2 = 'blue'
noun6 = 'stamp'
noun7 = 'queen'
verb4 = 'sneeze'



dictionary_letters = {
  'vowels': ['a', 'o', 'i', 'e', 'u'],
  'consonant': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
}




def verb_formatting(verb):

  """
  Checks the verb and changes the form of a verb for a sentense
  """

  if verb[-1] == 'y':
    formatted_verb = verb[:-1] + 'ies'

  elif verb == 'have':
    formatted_verb = verb[:-2] + 's'

  elif verb[-1] == 'o' or verb[-1] == 's' or verb[-1] == 'z' or verb[-1] == 'x' or (verb[-1] == 'c' and verb[-1] =='h'):
    formatted_verb = verb + 'es'    

  else:
    formatted_verb = verb + 's'
  return formatted_verb



def formatting_pronoun(noun):

  """
  Checks the noun whether it is a female or male noun  
  """

  if noun in dictionary_gender['female']:
    pronoun = 'she'

  elif noun in dictionary_gender['male']:
    pronoun = 'he'

  else:
    pronoun = 'it'
    
  return pronoun

def formatting_personal_pronoun(noun):
  """
  Checks the noun whether it is a female or male noun
  and places the correct personal pronoun when it is needed 
  """

  if noun in dictionary_gender['female']:
    pronoun = 'her'

  elif noun in dictionary_gender['male']:
    pronoun = 'him'

  else:
    pronoun = 'it'
    
  return pronoun


def verb_infinitive(verb):

  """
  Format verb into infinitive
  """

  if verb[-2] == 'i' and verb[-1] == 'e':
    infinitive_verb = verb[:-2] + 'ying'

  elif  verb[-1] == 'e':
    infinitive_verb = verb[:-1] + 'ing'

  elif verb[-2] in dictionary_letters['vowels'] and verb[-1] in dictionary_letters['consonant']:
    infinitive_verb  = verb + verb[-1] + 'ing'  

  else:
    infinitive_verb = verb + 'ing'

  return infinitive_verb




def plural_noun(noun):

  """
  Checks whether the noun is countable or not and transform into plural if it's countable
  """

  if noun in uncountable_nouns:
    return noun
  return pluralize(noun)



def choosing_article(word):

  """
  Checks which article to use before the word and place the article before it
  """

  if word[0] in dictionary_letters['vowels']:
    return f'an {word}'
  else: 
    return f'a {word}'



def choosing_a_quantifier(noun):

  """
  Checks whether the noun is countable or not and transform into plural if it's countable
  """

  if noun in uncountable_nouns:
    return 'some'
  return 'several'

def random_idiom():

  """
  Takes random idiom from the dictionary,
  Takes its meaning
  Takes 3 more meanings of random idioms from the dictionary
  Returns nested list
  """

  shuffle_idioms = list(idioms_dictionary.keys())
  random.shuffle(shuffle_idioms)
  shuffle_meanings = list(idioms_dictionary.values())
  random.shuffle(shuffle_meanings)
  # get_key_idiom = shuffle_idioms[0]
  # print(get_key_idiom)

  meanings = []

  main_meaning = idioms_dictionary[shuffle_idioms[0]]
  # print(main_meaning)
  meanings.append(main_meaning)

  

  for mean in range(3):
    mean = random.choice(shuffle_meanings)
    meanings.append(mean)
  random.shuffle(meanings)
  main_list = [shuffle_idioms[0], meanings]
  return main_list


idioms_list = random_idiom()


def run_the_time_error():
  """
  Prevent "RuntimeError: generator raised StopIteration"
  The package has raised StopIteration that was missed in python earier versions; thus, it worked before. 
  Since the package has not been updates since August 2018
  "PEP 479 is enabled for all code in Python >= 3.7, meaning that StopIteration exceptions raised directly or indirectly in coroutines and generators are transformed into RuntimeError exceptions."
  Link to this change:
  https://docs.python.org/3/whatsnew/3.7.html#changes-in-python-behavior
  """
  try:
    conjugate(verb = '', tense = PAST)
  except:
    pass

run_the_time_error()

madlib = f'''
{choosing_article(adj1).capitalize()} {noun1} {conjugate(verb1, tense = PAST)} and goes to a {adj2} {noun2}.
{formatting_pronoun(noun1).capitalize()} sees {famous_person.title()} {verb_infinitive(verb2)}.
{choosing_article(noun1).capitalize()}  and {famous_person.title()} decided to {verb3} and have {choosing_article(size_adjective1)} {color_adjective1} {noun3} together.
"It will cost an arm and a leg!" - sad the {noun1}.
"Do not worry!
I have a lot of {plural_noun(noun4)}!
I can afford it!"
"As you wish, {famous_person.title()}
You see, I am just a poor {noun1}... So I have only {plural_noun(noun5)}.
If you want to share {choosing_a_quantifier(noun4)} {plural_noun(noun4)}, let\'s get it!" - says the {noun1}.
And they started walking towards {choosing_article(size_adjective2)} {color_adjective2} {noun6}.
It was already night when {famous_person.title()} noticed {choosing_article(size_adjective2)} {noun6}.
"Can you see it? We are here!" - says {famous_person.title()} while pointing at the {noun6}.
"Oh, yes! But look at this old {noun7} in the bushes!" - says the {noun1}.
The old {noun7} started walking slowly towards {famous_person.title()} and the {noun1}.
Then, they saw that {formatting_pronoun(noun7)} was carrying a golden coin.
As soon as {formatting_pronoun(noun7)} reached our travelers, {formatting_pronoun(noun7)} started{verb_infinitive(verb4)} and handed out that golden coin to them and left silently.
{famous_person.title()} looked at the coin...
There were several words colored in {color_adjective2} and a big {color_adjective2} rose drawn under them.
"What is written there?" - asked the {noun1}.
"{idioms_list[0]}" - read out loud {famous_person.title()}.
"That's strange..." - {famous_person.title()} added.
"Why the text and the rose on the coin are {color_adjective2}?" - pondered the {adj1} {noun1}.
"Maybe because the {size_adjective2} {noun6} is {color_adjective2}?" - {famous_person.title()} replayed to {formatting_personal_pronoun(noun1)}.
As soon as they got closer to the {size_adjective2} {color_adjective2} {noun6}, they both yelled:

1. {idioms_list[1][0]}
2. {idioms_list[1][1]}
3. {idioms_list[1][2]}
'''

print(madlib)