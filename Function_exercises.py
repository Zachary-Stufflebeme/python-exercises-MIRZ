#1
def is_two(test):
    if test == 2 or test == '2':
        return True
    else:
        return False

#2
def is_vowel(test):
    if test in list('aeiouyAEIOUY'):
        return True
    else:
        return False

#3
def is_consonant(test):
    if not is_vowel(test) and test.isalpha() == True:
        return True
    else:
        return False
    
#4
def cap_first_con(test):
    new = ''
    count = 0
    for char in test:
        if is_consonant(char) == True and count == 0:
            new = new + char.capitalize()
            count = count + 1
        else:
            new = new + char
    return new
    
#5
def calculate_tip(percent , bill):
    return percent * bill

#6
def apply_discount(origP, percentage):
    return origP - (percentage * origP)

#7
def handle_commas(string):
    new = string.replace(',','')
    return new

#8
def get_letter_grade(numgrade):
    if numgrade >= 90:
        return('A')
    elif numgrade >= 80:
        return('B')
    elif numgrade >=70:
        return('C')
    elif numgrade >= 60:
        return('D')
    
#9
def remove_vowels(string):
    new = ''
    for char in string:
        if is_vowel(char) == False:
            new = new + char 
    return new
        
#10
def normalize_name(string):
    new = ''
    for char in string:
        new = new + char.lower()
    new = new.replace(' ','_')
    for char in new:
        if char.isidentifier() == False:
            new = new.replace(char,'')
    return new
        
#11
def cumulative_sum(listy):
    running_sum = 0
    new_listy = []
    for x in listy:
        running_sum += x
        new_listy.append(running_sum)
    return new_listy