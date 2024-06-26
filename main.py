import requests
import argparse
from print_color import print

def getword():
  argparser = argparse.ArgumentParser(description='Dictionary')
  argparser.add_argument('-w', '--word', type=str, help='Enter a word to search in dictionary')
  args = argparser.parse_args()

  if args.word:
    return args.word
  else:
    while True:
      arg = input('Enter your query: ')
      if isinstance(arg, str) and arg.strip():
        break
      else:
        print('Please enter a valid word.\n', color='red')
    return arg.strip()

def main():
  base_url = 'https://api.dictionaryapi.dev'
  word = getword()

  res = requests.get(f'{base_url}/api/v2/entries/en/{word}')
  json = res.json()
  if 'title' in json:
    print(json['title'])
    print(json['message'])
  else:
    json = json[0]
    phonetics = []
    meanings = []
    for ph in json['phonetics']:
      if 'text' in ph:
        phonetics.append(ph['text'])
    for meaning in json['meanings']:
      meaning_data = 'Part of Speech: ' + meaning['partOfSpeech'] + '\n' + 'Definition: ' + meaning['definitions'][0]['definition']
      if 'example' in meaning['definitions'][0]: meaning_data += '\nExample: ' + meaning['definitions'][0]['example']
      meanings.append(meaning_data)
    print(
      '\nWord: ' + word + '\n' +
      'Phonetics: ' + ', '.join(phonetics), color='white'
    )
    print('--------------------------------', color='green')
    for meaning in meanings:
      print(meaning, color='white')
      print('--------------------------------', color='green')

if __name__ == "__main__":
  main()
