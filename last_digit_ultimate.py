##############################################################
#### Arguments to be passed to the program like below:-
#### python last_digit_ultimate.py 12 11 522
#### total 3 nos are to be passed as parameter.
#### Mulitplication of Last Digit of 1st No and Last Digit of 2nd No should be equal to Last Digit of 3rd No
#### Output desired:-
#### Final Output: TRUE/FALSE
##############################################################

import sys
my_list = []

arg = sys.argv[1:]
for x in arg:
    my_list.append(x)

if(len(my_list) != 3):
    print('Wrong argument passed')
    print('python Calculator.py 12 11 52')
    sys.exit()

firstNoLastDigit  = int(my_list[0]) % 10
secondNoLastDigit = int(my_list[1]) % 10
thirdNoLastDigit  = int(my_list[2]) % 10

#print(firstNoLastDigit, " ", secondNoLastDigit, " ", thirdNoLastDigit)

if (firstNoLastDigit * secondNoLastDigit) == thirdNoLastDigit:
    print('Mulitplication of Last Digit of 1st No and Last Digit of 2nd No is equal to Last Digit of 3rd No')
    print('TRUE')
else:
    print('Mulitplication of Last Digit of 1st No and Last Digit of 2nd No is not equal to Last Digit of 3rd No')
    print('FALSE')