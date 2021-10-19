# Creating variables

adj1 = input('Type an adjective: ')
noun1 = input('Type a noun: ')
verb1 = input('Type a verb: ')

adj2 = input('Type an adjective: ')
noun2 = input('Type a noun: ')
famous_person = input("Type a famous person: ")
infinitive_verb = input('Type an infinitive verb: ')


dictionary_gender = {
  'female': ['girl', 'woman', 'lady', 'babygirl'],
  'male': ['man', 'boy', 'babyboy', 'gentleman', ]
}



def verb_formatting(verb1):

  """
  Checks the verb and changes the form of a verb for a sentense
  """

  if verb1[-1] == 'y':
    formatted_verb = verb1[:-1] + 'ies'

  elif verb1[-1] == 'o':
    formatted_verb = verb1 + 'es'
    

  else:
    formatted_verb = verb1 + 's'
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

madlib = f"A {adj1} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}. {formatting_pronoun(noun1)} sees {famous_person} {infinitive_verb}"

print(madlib)