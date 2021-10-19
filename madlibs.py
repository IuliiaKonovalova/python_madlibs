# Creating variables

adj1 = input('Type an adjective: ')
noun1 = input('Type a noun: ')
verb1 = input('Type a verb: ')

adj2 = input('Type an adjective: ')
noun2 = input('Type a noun: ')
famous_person = input("Type a famous person: ")
verb2 = input('Type a verb: ')


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

  elif verb[-1] == 'o':
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
  print(verb)
  if verb[-2] == 'i' and verb[-1] == 'e':
    infinitive_verb = verb[:-2] + 'ying'
  elif  verb[-1] == 'e':
    infinitive_verb = verb[:-1] + 'ing'
  elif verb[-2] in dictionary_letters['vowels'] and verb[-1] in dictionary_letters['consonant']:
    infinitive_verb  = verb + verb[-1] + 'ing'  
  else:
    infinitive_verb = verb + 'ing'
  return infinitive_verb

madlib = f"A {adj1} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}. {formatting_pronoun(noun1)} sees {famous_person} {verb_infinitive(verb2)}."

print(madlib)