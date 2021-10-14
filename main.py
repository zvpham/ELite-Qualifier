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

def check_errors(text, word):
  error  = 0
  incorrect_letter = 0
  #print(word)
  for i in range(len(text)):
    if(text[i] != word[i]):
      incorrect_letter += 1
      if(text[i] !=  word[i - 1] and text[i] != word[i + 1]):
        error += 1
  #print(error)
  return [error, incorrect_letter]

def ignore_words( word_list, words_shown_to_user):
  # words_to_ignore = []
  # print(words_shown_to_user)
  # print(word_list)
  ignore = input("do you want to ignore any words on the list (yes) or (no) ")
  while (ignore ==  "yes"):
    ignore_word = int(input("type in the number of the word "))
    word_list.remove(words_shown_to_user[ignore_word])

    ignore =  input("are there any more words you want to ignore (yes) or (no) ")



def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that

  possible_words = [

  ]

  possible_correct_words = [ 
    
  ]

  if text in all_words:
    print(text + ' is a word')
  else:
   for word in all_words:
     if(word[0] ==  text[0] and (len(word) >= len(text) - 1) and len(word) <= len(text) + 1):
       possible_words.append(word)

  for word in possible_words:
   # print(f" first instance of possible word - {word}")
    temp = word 
    errors =  0

    if(len(word) != len(text)):
      if(len(text) > len(word)):
        temp += "**"
        errors = check_errors(text, temp)
      else:
        errors = check_errors(text,temp)
    else:
      temp += "*"
      errors = check_errors(text,temp)

    if(errors[0] <= 1):
      possible_correct_words.append(word)
    
  #print(possible_correct_words)
  for i in range(len(possible_correct_words)):
    print(f"did you mean [{i}] {possible_correct_words[i]}")
  
  if(len(possible_correct_words) > 0):
    choice =  int(input(" type in the number of the word you mean to type "))
    real_word = possible_correct_words[choice]
  else:
    real_word = text

  ignore_words(all_words ,possible_correct_words)
  real_word += " "
  return real_word

def main():
    all_words = load_words()
    sentence = ""
    while True:
        print('Type some text, or type \"quit\" to stop')
        text = input(':> ')
        if ('quit' == text):
          print(sentence)
          break
        sentence += suggest(text, all_words)

        

if __name__ == "__main__":
    main()

