# Creating variables

adj1 = input('Type an adjective: ')
noun1 = input('Type a noun: ')
verb1 = input('Type a verb: ')

adj2 = input('Type an adjective: ')
noun2 = input('Type a noun: ')
famous_person = input("Type a famous person: ")
infinitive_verb = input('Type an infinitive verb: ')



def verb_formatting(verb1):

  """
  Checks the verb and changes the form of a verb for a sentense
  """
  
  if verb1[-1] == 'y':
    verb1[-1] == 'i'
    formatted_verb = verb1 + 's'
    return formatted_verb

  elif verb1[-1] == 'o':
    formatted_verb = verb1 + 'es'
    return formatted_verb

  else:
    formatted_verb = verb1 + 's'
    return formatted_verb



madlib = f"A {adj1} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}. She sees {famous_person} {infinitive_verb}"

print(madlib)