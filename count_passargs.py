##############################################################
#### Arguments to be passed to the program like below:-
#### python count_passargs.py hello world america
#### Find the total nos of vowels, consonants and words.
#### Output desired:-
#### Vowels: 7  Consonants:  10  Words:  3
##############################################################
import sys

my_list = []
vowels = 0
consonant = 0
words = 0

arg = sys.argv[1:]
for x in arg:
    my_list.append(x)

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for i in range(0, len(my_list)):
    word = my_list[i]
    if(is_intstring(word)):
        words = 0
    else:
        words += 1
    for i in range(0, len(word)):
        ch = word[i]
        if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            ch = ch.lower()
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

print("Vowels:", vowels, " Consonants: ", consonant, " Words: ", words)