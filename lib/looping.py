#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0 :
        print(i)
        i -= 1

    print("Happy New Year!")
happy_new_year()    

def square_integers(int_list):
    # code goes here!
    new_list = [num ** 2 for num in int_list ]
    return new_list

square_integers([])    

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
       if i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz")
       elif i % 3 == 0:
           print('Fizz')  
       elif i % 5 == 0:
           print('Buzz')  
       else :
           print (i)  
fizzbuzz()           
