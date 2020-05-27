##############################################################
#### Arguments to be passed to the program like below:-
#### python facebook_profile_photo.py
#### Parameter to be passed should be square length, no of photos & dimension of photos in width and height.
#### [1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
#### [2] If width and height, both are large enough and
#### (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
#### (b) else user is prompted to crop it. Print "CROP IT" in this case.
#### Output desired:-
#### Final Output: "UPLOAD ANOTHER"/ACCEPTED/"CROP IT"
##############################################################

import sys, string
min_photo_length = input()
no_of_photos = input()

no_of_lines = int(no_of_photos)
lines = []
for i in range(no_of_lines):
    lines.append(input())

def contains_whitespace(s):
    return True in [c in s for c in string.whitespace]

for i in range(len(lines)):
    try:
        x,y = lines[i].split(' ',1)
        if (contains_whitespace(y)):
            print('you have provided wrong inputs, the second number should not contain spaces, please provide correct information again.')
            sys.exit()
        if (int(x)>=int(min_photo_length)) and (int(y)>=int(min_photo_length)) and (int(x)==int(y)):
            print('ACCEPTED')
        elif (int(x)>=int(min_photo_length)) and (int(y)>=int(min_photo_length)) and (int(x)!=int(y)):
            print('CROP IT')
        else:
            print('UPLOAD ANOTHER')
    except:
        print('you have provided wrong inputs, please provide correct information again.')
        sys.exit()