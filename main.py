import hm_ascii_art as hm_module
import random

def get_random_word(word_list):
  """ This function returns a random string from the passed list of strings."""
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]


def play_again():
  """This function returns True if the player wants 
  to play again; otherwise, it returns False. """
  print ("Do you want to play again? (yes or no)")
  return input().lower().startswith("y")
print("You answered: ", play_again())

def get_random_word(word_list):
  """ This function returns a random string from the passed list of strings."""
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]


def play_again():
  """This function returns True if the player wants 
  to play again; otherwise, it returns False. """
  print ("Do you want to play again? (yes or no)")
  return input().lower().startswith("y")
print("You answered: ", play_again())