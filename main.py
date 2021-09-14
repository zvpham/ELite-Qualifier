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
  print(word)
  for i in range(len(text)):
    if(text[i] != word[i]):
      if(text[i] !=  word[i - 1] or text[i] != word[i + 1] and i != len(text)):
        error += 1
        if(word == "dog" or text == "dog"):
          print(word[i])
          print(text[i])
  return error



def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that

  possible_words = [

  ]

  if text in all_words:
    print(text + ' is a word')
  else:
   for word in all_words:
     if(word[0] ==  text[0] and (len(word) >= len(text) - 1) and len(word) <= len(text) + 1):
       possible_words.append(word)

  
  for word in possible_words:
    print(f"first word {word}")
    temp = word 
    error =  0
    if(len(word) != len(text)):
      if(len(text) > len(word)):
        print("word less length")
        temp += "**"
        error = check_errors(text, temp)
      else:
        print("word greater length")
        print(f"helllo len(temp)")
        error = check_errors(text,temp)
    else:
      print("word equal length")
      temp += "*"
      error = check_errors(text,temp)

    if(error > 1):
      possible_words.remove(word)
      print(len(possible_words))

    
  print(possible_words)


    

def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

