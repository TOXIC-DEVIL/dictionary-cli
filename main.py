import requests
import argparse

def getword():
  argparser = argparse.ArgumentParser(description='Dictionary')
  argparser.add_argument('-w', '--word', type=str, help='Enter a word to search in dictionary')
  args = argparser.parse_args()

  if args.word:
    return args.word
  else:
    while True:
      arg = input('Enter your query: ')
      if isinstance(arg, str):
        break
    return arg

def main():
  getword()
  # to-do

if __name__ == '__main__':
  main()