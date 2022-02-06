# create an app that checks if the word is a palindrome
# example:
# if the word is "racecar" then it would turn true since "racecar" backwards is still "racecar"
# if the word is "hill" then it would return false since "hill" backwards is "llih"
 
import argparse

parser = argparse.ArgumentParser(description='enter a word')

parser.add_argument('word',type=str)

args = parser.parse_args()

# main function

def palindroma(word):
    reversedWord = ''.join(reversed(word))
    if word == reversedWord:
        print('this is a palindrome')
    else:
        print('this is not a palindrome')

palindroma(args.word)
