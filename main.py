#@author: github.com/guidoenr4
#@date: 07-09-2020

from random import randrange

def test_cases(cases):
    changin = 0
    staying = 0
    i = 0
    while i < cases:
        doors = new_case()
        correct = get_correct(doors)
        choice = randrange(3)
        if switch(doors, correct, choice):
            changin+=1
        else:
            staying+=1
        i+=1
    print("Changin: " + str(changin) + " cases" )
    print("Staying: " + str(staying) + " cases" )

def switch(doors, correct, choice):
    return not choice == correct

def get_correct(doors):
    i = 0
    for x in doors:
        if x == True:
            return i
        else:
            i+=1

def new_case():
    random = randrange(3)
    doors_array = [False, False, False]
    doors_array[random] = True
    return doors_array

if __name__ == '__main__':
    print("monty hall paradox por guidoti")
    cases = int(input("cases: "))
    test_cases(cases)
