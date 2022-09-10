# -*- coding: utf-8 -*-
"""coding1
"""
'''
Returns whether the first letter of string s is a vowel.
Parameters:
s (string): lowercase string without spaces, numbers, or special characters.
Returns:
bool: True if starts with a vowel, False otherwise
'''
def is_vowel(s):

  if s[0] in 'aeiou':
    vowel_start = True
  else:
    vowel_start = False

  return vowel_start # bool


'''
Returns the pig-latin equivalent of a given string s.
Parameters:
s (string): lowercase string without spaces, numbers, or special characters.
Returns:
str: pig-latinized word
'''
def piggify(s):

  firstLetter = is_vowel(s[0])
  secondLetter = is_vowel(s[1])

  if firstLetter == True:
    pig_latinized = s + 'way'
  elif firstLetter == False and secondLetter == True:
    pig_latinized = s[1:] + s[0] + 'ay'
  else:
    pig_latinized = s[2:] + s[0] + s[1] + 'ay'

  return pig_latinized 

'''
Returns the pig-latin equivalent of a sentence.
Parameters:
sentence (string): A string of a sentence.
Returns:
str: the pig-latinized senetence.
'''
def piggify_sentence(sentence):

    output = ''

    words = [word.lower() for word in sentence.split(' ')]
 
    for word in words:
      i = 1
      if word[-i] in '.?!,':
        output += piggify(word[0:-1]) + word[-i] + ' '
      else:
        output += piggify(word) + ' '

      i+=1

    piggied_sentence = output.rstrip()

    return piggied_sentence #str
'''
Returns a code decoder dictionary
Parameters: 
secret_alphabet (string): a 26 letter string of unique characters without spaces.
Returns:
dict: a dictionary mapping from each secret language letter to its english alphabet
equivalent.
'''
def create_code(secret_alphabet):

    decoder = {secret_alphabet[0]:'a', secret_alphabet[1]:'b', secret_alphabet[2]:'c', 
                 secret_alphabet[3]:'d', secret_alphabet[4]:'e', secret_alphabet[5]:'f', secret_alphabet[6]:'g', 
                 secret_alphabet[7]:'h', secret_alphabet[8]:'i', secret_alphabet[9]:'j', secret_alphabet[10]:'k', 
                 secret_alphabet[11]:'l', secret_alphabet[12]:'m', secret_alphabet[13]:'n', secret_alphabet[14]:'o', 
                 secret_alphabet[15]:'p', secret_alphabet[16]:'q', secret_alphabet[17]:'r', secret_alphabet[18]:'s', 
                 secret_alphabet[19]:'t', secret_alphabet[20]:'u', secret_alphabet[21]:'v', secret_alphabet[22]:'w', 
                 secret_alphabet[23]:'x', secret_alphabet[24]:'y', secret_alphabet[25]:'z'}

    return decoder # dict
'''
Returns the decoded version of a string using a decoder dictionary
Parameters:
decoder (dict): a dictionary mapping from each secret language letter to its 
english alphabet equivalent.
encoded_word (str): a string made up only of characters in the secret language.
Returns:
str: the decoded word.
'''
def decode(decoder, encoded_word):

    decoded_word = ''
    word_length = len(encoded_word)

    i = 0
    while i < word_length:
      decoded_word = decoded_word + decoder[encoded_word[i]]
      i = i + 1

    return decoded_word # str
'''
Returns an integer that is the nth Fibonacci number.
Parameters:
n (int): The nth Fibonacci number you want.
Returns:
int: the nth fibonacci number.
'''
def recursive_fib(n):
    
    if n == 0:
      fib_n = 0
    elif n == 1 or n == 2:
      fib_n = 1
    else:
      fib_n = recursive_fib(n - 1) + recursive_fib(n - 2)

    return fib_n # int
'''
Returns an integer that is the nth Fibonacci number.
Parameters:
n (int): The nth Fibonacci number you want.
Returns:
int: the nth fibonacci number.
'''
def iterative_fib(n):

    if(n == 0):
      return 0;
    else:
      x = 0
      y = 1
      for i in range(1, n):
        z = (x + y)
        x = y
        y = z

    fib_n = y

    return fib_n # int

######################################################################
### Testers Below!!! ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 1: Python Introduction!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Pig-Latin and Codes")
    print("---------------------------------------")
  
    print("---------------------------------------")
    print("\'is_vowel\' Tests")
    print("---------------------------------------")
    is_vowel_tests = ['apple', 'cake', '...hi', 'eating']
    is_vowel_answers = [True, False, False, True]
  
    for count, test in enumerate(is_vowel_tests):
        if (is_vowel(is_vowel_tests[count]) == is_vowel_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_vowel_answers[count]}')
        print(f'Your Answer: {is_vowel(is_vowel_tests[count])}')
    print("---------------------------------------")
    print("\'piggify\' Tests")
    print("---------------------------------------")
    piggify_tests = ['cake', 'icecream', 'treat', 'apple', 'walk']
    piggify_answers = ['akecay', 'icecreamway', 'eattray', 'appleway', 'alkway']
  
    for count, test in enumerate(piggify_tests):
        if (piggify(piggify_tests[count]) == piggify_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {piggify_answers[count]}')
        print(f'Your Answer: {piggify(piggify_tests[count])}')
      
    print("---------------------------------------")
    print("\'piggify_sentence\' Tests")
    print("---------------------------------------")
    piggify_sentence_tests = ['The boy, Sam, walked to the store.', \
                              'Hello, how are you?', \
                              'Discrete math is so much fun!']
    piggify_sentence_answers = ['ethay oybay, amsay, alkedway otay ethay orestay.',
\
                                'ellohay, owhay areway ouyay?', \
                                'iscreteday athmay isway osay uchmay unfay!']
   
    for count, test in enumerate(piggify_sentence_tests):
        if (piggify_sentence(piggify_sentence_tests[count]) == 
piggify_sentence_answers[count]):
            passed = 'PASSED!'
        else:
            passed = 'FAILED!'
        
        print("Test #{}: {}".format(count + 1, passed))   
        print(f'Correct Answer: {piggify_sentence_answers[count]}')
        print(f'Your Answer: {piggify_sentence(piggify_sentence_tests[count])}')
    
    print("---------------------------------------")
    print("\'create_code\' Tests")
    print("---------------------------------------")
    alphabet_1 = 'Hh!@mbM*()QWERTYUIOPASDFGZ'
    decoder_1={'H': 'a', 
               'h':'b',
               '!':'c',
               '@': 'd',
               'm': 'e', 
               'b': 'f',
               'M': 'g', 
               '*': 'h', 
               '(': 'i',
               ')':'j',
               'Q': 'k', 
               'W': 'l', 
               'E':'m',
               'R': 'n', 
               'T': 'o', 
               'Y':'p', 
               'U': 'q', 
               'I':'r',
               'O': 's', 
               'P':'t',
               'A':'u',
               'S':'v', 
               'D': 'w', 
               'F': 'x', 
               'G': 'y',
               'Z': 'z'}
    alphabet_2 = 'Hh!@mbM*()qwertyUIOPAS5FGZ'
    decoder_2={'H': 'a', 
               'h':'b',
               '!':'c',
               '@': 'd', 
               'm': 'e', 
               'b': 'f',
               'M': 'g', 
               '*': 'h', 
               '(': 'i',
               ')':'j',
               'q': 'k', 
               'w': 'l', 
               'e':'m',
               'r': 'n', 
               't': 'o', 
               'y':'p', 
               'U': 'q',
               'I':'r',
               'O': 's', 
               'P':'t',
               'A':'u',
               'S':'v', 
               '5': 'w', 
               'F': 'x', 
               'G': 'y',
               'Z': 'z'}
    create_code_tests = [alphabet_1, alphabet_2]
    create_code_answers = [decoder_1, decoder_2]
    for count, test in enumerate(create_code_tests):
        if (create_code(create_code_tests[count]) == create_code_answers[count]):
            passed = "PASSED!"
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed)) 
        print(f'Correct Answer: {create_code_answers[count]}')
        print(f'Your Answer: {create_code(create_code_tests[count])}')
    
    print("---------------------------------------")
    print("\'decode\' Tests")
    print("---------------------------------------")
    decode_tests = [[decoder_1, '@TM'], [decoder_2, '!HP']]
    decode_answers = ['dog', 'cat']
    for count, test in enumerate(decode_tests):
        if (decode(decode_tests[count][0], decode_tests[count][1]) == 
decode_answers[count]):
            passed = 'PASSED!'
        else:
            passed = 'FAILED!'
            
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {decode_answers[count]}')
        print(f'Your Answer: {decode(decode_tests[count][0], decode_tests[count][1])}')
    
    print()
    print("---------------------------------------")
    print("PART B: Fibonacci")
    print("---------------------------------------")
    tests = [[1, 1], [4, 4], [10, 10]]
    answers = [[1, 1], [3, 3], [55, 55]]
    for count, test in enumerate(tests):
        if(answers[count][0] == recursive_fib(test[0]) and
            answers[count][1] == iterative_fib(test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"
    
        print("Test #{}: {}".format(count + 1, passed))
        print("Recursive Fibonacci (Correct): ", answers[count][0])
        print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
        print("Iterative Fibonacci (Correct): ", answers[count][1])
        print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))

