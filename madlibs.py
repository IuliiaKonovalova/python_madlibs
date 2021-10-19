
import re, requests, json

# Creating variables

adj1 = input('Type an adjective: ')
noun1 = input('Type a noun: ')
verb1 = input('Type a verb: ')

adj2 = input('Type an adjective: ')
noun2 = input('Type a noun: ')
famous_person = input("Type a famous person: ")
verb2 = input('Type a verb: ')

verb3 = input('Type a verb: ')
noun3 = input('Type a noun: ')
color_adjective = input('Type a color adjective: ')
size_adjective = input('Type a size adjective: ')

noun4 = input('Type a noun: ')



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

  elif verb[-1] == 'o' or verb[-1] == 's':
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
	'''
	searches Google NGram to see if a word is a countable or not
	'''

	# format into url (replace spaces with + for url)
	thing = re.sub(' ', '\+', noun)
	url = 'https://books.google.com/ngrams/graph?content=many+' + noun + '%2C+much+' + noun + '&year_start=1800&year_end=2000'
	response = requests.get(url)
	html = response.read()

	# extract timeseries data from html source
	# if an error thrown, it's likely there's no match for the term
	thing = re.sub('\+', ' ', noun)
	try:
		many_data = json.loads(re.search('\{"ngram": "many ' + noun + '".*?\}', html, re.IGNORECASE).group(0))['timeseries']
		many = sum(many_data) / float(len(many_data))
	except:
		many = 0.0

	try:
		much_data = json.loads(re.search('\{"ngram": "much ' + thing + '".*?\}', html, re.IGNORECASE).group(0))['timeseries']
		much = sum(much_data) / float(len(much_data))
	except:
		much = 0.0

	# return True if countable; False if not
	if many > much:
		return noun + 's'
	return noun

madlib = f'A {adj1} {noun1} {verb_formatting(verb1)} and goes to a {adj2} {noun2}.\n{formatting_pronoun(noun1)} sees {famous_person} {verb_infinitive(verb2)}.\n{noun1.capitalize()}  and {famous_person} decide to {verb3} and have a {color_adjective} {size_adjective} {noun3} together.\n"It will cost an arm and a leg!" - sad {noun1}.\n"Do not worry! I have {plural_noun(noun4)}'

print(madlib)