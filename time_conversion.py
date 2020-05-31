##############################################################
#### Arguments to be passed to the program like below:-
#### python time_conversion.py
#### Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#### Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

#### Sample Input: 07:05:45PM
#### Hence Output will be 19:05:45
##############################################################

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    string_len = len(s)
    tym = ''
    am_or_pm = s[-2:]
    hours = s[0: 2:]
    rest_tym = s[2: string_len-2:]
    if am_or_pm == 'PM' and hours != '12':
        hours = int(hours) + 12
        tym = str(hours) + rest_tym
    elif am_or_pm == 'PM' and hours == '12':
        tym = str(hours) + rest_tym
    elif am_or_pm == 'AM':
        if hours == '12':
            tym = '00' + rest_tym
        else:
            tym = str(hours) + rest_tym 
    return tym

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    print(result)
    f.write(result + '\n')
    f.close()