##############################################################
#### Arguments to be passed to the program like below:-
#### python annoyingShortListCriteria.py 2 Seeta Sita
#### total 3 nos are to be passed as parameter.
#### Mulitplication of Last Digit of 1st No and Last Digit of 2nd No should be equal to Last Digit of 3rd No
#### Output desired:-
#### Final Output: TRUE/FALSE
##############################################################

import sys, string
my_list = []
applicant_name_length = 0
find_divisor_number = 0

arg = sys.argv[1:]
for x in arg:
    my_list.append(x)

noOfApplicant = my_list[0]

def letter_to_int(letter):
    if(letter.islower()):
        return ord(letter) - ord("a") + 1
    else:
        letter=letter.lower()
        return ord(letter) - ord("a") + 1

def divCount(n): 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
  
    # Traversing through  
    # all prime numbers 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1):
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1);                  
    return total; 

if(len(my_list) != int(noOfApplicant)+1):
    print('Wrong argument passed')
    sys.exit()
else:
    print('lets continue!')
    for i in range(1, len(my_list)):
        applicant_name = my_list[i]
        for i in range(0, len(applicant_name)):
            applicant_name_length += letter_to_int(applicant_name[i])
        find_divisor_number = divCount(applicant_name_length)
        actual_application_length = len(applicant_name)
        if(actual_application_length > find_divisor_number):
            print('applicant ', applicant_name, ' is OUT')
        else:
            print('applicant ', applicant_name, ' is IN')
        applicant_name_length = 0
    
    