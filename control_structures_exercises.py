#1a
print( 'What day is today?')
today = input()
if today == 'Monday': 
    print('Today IS Monday')
else:
    print('Today IS NOT Monday')
#1b
print( 'What day is today?')
today = response
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
if today in weekdays:
    print('Today is a weekday.')
else:
    print('Today is the weekend.')
#1c
weekly_hours_worked = 55
hourly_rate = 10000
if weekly_hours_worked > 40:
    overtime = weekly_hours_worked - 40
    paycheck = (weekly_hours worked * hourly_rate) + (overtime * (hourly_rate *1.5))
else:
    paycheck = hourly_rate * weekly_hours_worked

    
#2a

i = 5
while i < 15:
    print(i)
    i = i + 1

i = 0 
while i <= 100:
    print(i)
    i = i + 2
    
i = 100
while i >= -10:
    print(i)
    i = i - 5
    
i = 2
while i < 1000000:
    print(i)
    i = i ** 2
    
i = 100
while i > 0:
    print(i)
    i = i - 5
    
#2b

print('Please input number')
answer = input()
for number in range(1,answer):
    print(answer '*' number ' = ' answer * number)
    
for number in range(1,10):
    strnumber = str(number)
    print(strnumber * number)
    
#2c

print('Please input positive number')
answer = input
i = answer
while i > 0:
    print(i)
    i = i - 1
    
print('Please input a positive number')
input.astype(int)
if input > 0:
    answer = input
for number in range(1,answer)
print(number)


print('Please input odd number between 1 and 50')
if input.astype(int) >1 and input.astype(int) < 50 :
    i = input 
    for number in range(1,50):
        if number % 2 != 0 and number != i:
            print(number)
else:
    print('Please input odd number between 1 and 50')
    
#3
for numbers in range(1,101)
print(numbers)



for numbers in range(1,100):
    if numbers % 3 == 0:
        print('fizz')
    else:
        print(numbers)
        

        
for numbers in range(1,100):
    if numbers % 3 == 0:
        print('fizz')
    if numbers % 5 == 0:
        print('buzz')
    else:
        print(numbers)
        



for numbers in range(1,100):
    if numbers % 3 == 0:
        print('fizz')
    if numbers % 5 == 0:
        print('buzz')
    if (numbers % 3 == 0) and (numbers % 5 == 0):
        print('fizzbuzz')
    else:
        print(numbers)

    

    
#4

print('Please enter an integer')
user_num = int(input)
for i in range(1, user_num + 1):
    print(f'{i}  | {i**2}  | {i**3}')
user_yn = input('Continue?')
if user_yn = 'no':
    break