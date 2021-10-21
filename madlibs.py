
import nltk


nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

from pattern.en import pluralize

import random

from uncountable_nouns import uncountable_nouns
from idioms import idioms_dictionary



# Creating variables

adj1 = input('Type an adjective: ')
noun1 = input('Type a noun (living thing): ')
verb1 = input('Type a verb: ')

adj2 = input('Type an adjective: ')
noun2 = input('Type a noun: ')
famous_person = input("Type a famous person: ")
verb2 = input('Type a verb: ')

verb3 = input('Type a verb: ')
noun3 = input('Type a noun: ')
size_adjective1 = input('Type a size adjective: ')
color_adjective1 = input('Type a color adjective: ')

noun4 = input('Type a noun: ')
noun5 = input('Type a noun: ')

size_adjective2 = input('Type a size adjective: ')
color_adjective2 = input('Type a color adjective: ')
noun6 = input('Type a noun: ')

noun7 = input('Type a noun (living thing): ')
verb4 = input('Type a verb: ')





dictionary_gender = {
  'female': ['girl', 'woman', 'lady', 'babygirl'],
  'male': ['man', 'boy', 'babyboy', 'gentleman', ]
}

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
  format verb into infinitive
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
  get_key_idiom = shuffle_idioms[0]
  print(get_key_idiom)

  meanings = []

  main_meaning = idioms_dictionary[shuffle_idioms[0]]
  print(main_meaning)
  meanings.append(main_meaning)
  print(meanings)
  

  for mean in range(3):
    mean = random.choice(shuffle_meanings)
    meanings.append(mean)
  main_list = [shuffle_idioms[0], meanings]
  return main_list





madlib = f'''
{choosing_article(adj1).capitalize()} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}.
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
As soon as {formatting_pronoun(noun7)} reached our travelers, {formatting_pronoun(noun7)} {verb4} and handed out that golden coin to them and left silently.
{famous_person.title()} looked at the coin...
There were several words colored in {color_adjective2} and a big {color_adjective2} rose drawn under them.
"What is written there?" - asked the {noun1}.
"{random_idiom()[0]}" - read out loud {famous_person.title()}.
"That's strange..." - {famous_person.title()} added.
"Why the text and the rose on the coin are {color_adjective2}?" - pondered the {adj1} {noun1}.
"Maybe because the {choosing_article(size_adjective2)} {noun6} is {color_adjective2}?" - {famous_person.title()} replayed to {formatting_personal_pronoun(noun1)}.
As soon as they got closer to the {size_adjective2} {color_adjective2} {noun6}, they both yelled:

1. {random_idiom()[1][0]}
2. {random_idiom()[1][1]}
3. {random_idiom()[1][2]}
'''

print(madlib)