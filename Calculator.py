##############################################################
#### Arguments to be passed to the program like below:-
#### python Calculator.py 12 10 add
#### addition/substract/multiply/division/add/sub/mult/div valid arithmetic parameter
#### Output desired:-
##############################################################

import sys
my_list = []
output = 0

arg = sys.argv[1:]
for x in arg:
    my_list.append(x)

if(len(my_list) != 3):
    print('Wrong argument passed')
    print('python Calculator.py 12 10 add')
    print('Correct arithmetic operation: add/sub/mult/div')
    sys.exit()

if int(my_list[0]) < 0 or int(my_list[1]) < 0:
    print('Negative Nos are passed as argument')
    print('Expected Nos should be greater than 0 should be passed as argument')
    sys.exit()

if ((my_list[2] != "add") and (my_list[2] != "sub") and (my_list[2] != "mult") and (my_list[2] != "div")):
    print('wrong arithemetic argument passed')
    sys.exit()
else:
    print('Okay lets proceed')
    if (my_list[2] == 'add') or (my_list[2] == 'addition'):
        output = int(my_list[0]) + int(my_list[1])
        print('Addition of 2 nos.:', output)
    elif (my_list[2] == 'sub') or (my_list[2] == 'substract'):
        output = int(my_list[0]) - int(my_list[1])
        print('Substraction of 2 nos.:', output)
    elif (my_list[2] == 'mult') or (my_list[2] == 'multiply'):
        output = int(my_list[0]) * int(my_list[1])
        print('Multiplication of 2 nos.:', output)
    elif (my_list[2] == 'div') or (my_list[2] == 'divide'):
        try:
            output = int(my_list[0]) / int(my_list[1])
            print('Division of 2 nos.:', output)
        except ZeroDivisionError as error:
            print('0 has been passed as 2nd no with division as arithmentic operation which is not desired.')
            sys.exit()
