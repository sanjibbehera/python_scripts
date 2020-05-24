##################################################################################################
#### HackerEarth program to be executed like below:-
#### python GokiNhisBreakup.py
#### First Input denotes the number of People.
#### Second Input denotes the minimum number of skill in the People to be friends with Goki.
#### Output desired:-
#### Final Output: YES/NO
##################################################################################################

no_of_frns = input()
checkpoint = input()
no_of_lines = int(no_of_frns)
lines = []
for i in range(no_of_lines):
    lines.append(input())

for idx, line in enumerate(lines):
    if(int(line) >= int(checkpoint)):
        print('YES')
    else:
        print('NO')

