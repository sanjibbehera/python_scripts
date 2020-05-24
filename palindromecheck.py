##################################################################################################
#### HackerEarth program to be executed like below:-
#### python palindromecheck.py
#### Single string to be passed when prompted to check if it the string is palindrome.
#### Output desired:-
#### Final Output: YES/NO
##################################################################################################

x=input("")

if(x==x[::-1]):
    print('YES')
else:
    print('NO')