import time
# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words

"""
Parameters: user_word - the word that the user inputed,
            word -  a word that the code believes could be similar to user_word

Function: Compares the User's word to a word in the list possible_words and returns an integer of how many letters did not match within a range of one space between both words  
"""
def check_errors(user_word, word):
  error  = 0
  for i in range(len(user_word)):
    if(user_word[i] != word[i]):
      if(user_word[i] !=  word[i - 1] and user_word[i] != word[i + 1]):
        error += 1
  return error

"""
Parameters: word_list - a list of all possible words 
            words_shown_to_user - list of words that were shown to user to likely be the one they meant to type

Function: asks the user if they want to remove a word from word_list and if yes choose which words out of words_shown_to_user to remove from it for the rest of the programs runtime
"""
def ignore_words( word_list, words_shown_to_user):
  ignore = input("do you want to ignore any words on the list (yes) or (no) ")
  while (ignore ==  "yes"):
    ignore_word = int(input("type in the number of the word "))
    word_list.remove(words_shown_to_user[ignore_word])
    print("")
    ignore =  input("are there any more words you want to ignore (yes) or (no) ")


"""
Parameters: all_words - a list of all possible words 
            user_word - a word that the user inputed

Function: The user inputs a word and if it isn't a word in safedict_simple suggest a word that could be the word that the user inteded to type
"""
def suggest(user_word, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that

  possible_words = []
  possible_correct_words = [ ]

  # checks to see if the word the user inputed was a word found in safedict_simple and if no create a list of possible words that they meant to type
  if user_word in all_words:
    print(user_word + ' is a word')
  else:
   for word in all_words:
     if(word[0] ==  user_word[0] and (len(word) >= len(user_word) - 1) and len(word) <= len(user_word) + 1):
       possible_words.append(word)

  # finds amount of or letters that aren't the same within a range of one place between the word the user inputed and a possible word
  for word in possible_words:
    temp = word 
    errors =  0

    if(len(word) != len(user_word)):
      if(len(user_word) > len(word)):
        temp += "**"
        errors = check_errors(user_word, temp)
      else:
        errors = check_errors(user_word,temp)
    else:
      temp += "*"
      errors = check_errors(user_word,temp)

    if(errors <= 1):
      possible_correct_words.append(word)

  if len(possible_correct_words) == 0:
    print(f"{user_word} isn't a word")
    return ""

  for i in range(len(possible_correct_words)):
    print(f"did you mean [{i}] {possible_correct_words[i]}")
  print("")

  
  if(len(possible_correct_words) > 0):
    choice =  int(input(" type in the number of the word you mean to type "))
    real_word = possible_correct_words[choice]
    print("")
    ignore_words(all_words ,possible_correct_words)
  else:
    real_word = user_word

  real_word += " "
  return real_word

def main():
    all_words = load_words()
    sentence = ""
    while True:
        print('Type some text, or type \"quit\" to stop')
        user_word = input(':> ')
        if ('quit' == user_word):
          print(sentence)
          break
        sentence += suggest(user_word, all_words)
        print(f"sentence so far: {sentence}")

        

if __name__ == "__main__":
    main()

