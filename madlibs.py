
import nltk


nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

from uncountable_nouns import uncountable_nouns

from pattern.en import pluralize

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



def formatting_pronoun(noun1):

  """
  Checks the noun1 whether it is a female or male noun  
  """

  if noun1 in dictionary_gender['female']:
    pronoun = 'she'

  elif noun1 in dictionary_gender['male']:
    pronoun = 'he'

  else:
    pronoun = 'it'
    
  return pronoun.capitalize()




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
  Checks
  """

  if word[0] in dictionary_letters['vowels']:
    return f'a {word}'
  else: 
    return f'n {word}'



def choosing_a_quantifier(noun):

  """
  Checks whether the noun is countable or not and transform into plural if it's countable
  """

  if noun in uncountable_nouns:
    return 'some'
  return 'several'


madlib = f'''
{choosing_article(adj1).capitalize()} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}.
{formatting_pronoun(noun1)} sees {famous_person.title()} {verb_infinitive(verb2)}.
{noun1.capitalize()}  and {famous_person.title()} decide to {verb3} and have {choosing_article(size_adjective1)} {color_adjective1} {noun3} together.
"It will cost an arm and a leg!" - sad {noun1}.
"Do not worry!
I have a lot of {plural_noun(noun4)}!
I can afford it!"
"As you wish, {famous_person.title()}
You see, I am just a poor {noun1}... So I have only {plural_noun(noun5)}.
If you want to share {choosing_a_quantifier(noun4)} {plural_noun(noun4)},let\'s get it!" - says {noun1}.
And they started walking towards {choosing_article(size_adjective2)} {color_adjective1} {noun6}.'''

print(madlib)