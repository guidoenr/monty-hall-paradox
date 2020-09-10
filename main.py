#@author: github.com/guidoenr4
#@date: 07-09-2020

import bcolors, time
from random import randrange

def test_cases(cases):
    changing = 0
    staying = 0
    bcolors.print_warning("Testing..")
    for i in range(0, cases):
        correct, choice = new_case()
        if not choice == correct : changing+=1
        else : staying+=1
    bcolors.print_green("changing the door: " + str(changing) + " cases" )
    bcolors.print_blue("staying with your decision: " + str(staying) + " cases" )


def new_case():
    return randrange(3), randrange(3)

if __name__ == '__main__':
    bcolors.print_best("MONTY-HALL PARADOX, @author> guidoenr4")
    cases = int(input("insert the cases to test (with 3 doors): "))
    start_time = time.time()
    test_cases(cases)
    bcolors.print_curl('seconds: ' + str(time.time() - start_time))


