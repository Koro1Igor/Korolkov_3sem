import math
import sys

REQUIRED_NUMBER_OF_ARGUMENTS = 4
MIN_NUMBER_OF_ARGUMENTS = 1

def IsQuantityArgsCorrect():
    if len(sys.argv) > REQUIRED_NUMBER_OF_ARGUMENTS:
        print("Too many arguments entered, please try again" '\n')
        calculate_roots(get_coeff_a(), get_coeff_b(), get_coeff_c())

    elif len(sys.argv) < REQUIRED_NUMBER_OF_ARGUMENTS and len(sys.argv) != MIN_NUMBER_OF_ARGUMENTS:
        print("Too few arguments entered, please try again" '\n')
        calculate_roots(get_coeff_a(), get_coeff_b(), get_coeff_c())
    
    elif len(sys.argv) == MIN_NUMBER_OF_ARGUMENTS:
        calculate_roots(get_coeff_a(), get_coeff_b(), get_coeff_c())
        
    else:
 
        coeff_a = Check_correctness_coefficient_from_arg(sys.argv[1], "a")
        coeff_b = Check_correctness_coefficient_from_arg(sys.argv[2], "b")
        coeff_c = Check_correctness_coefficient_from_arg(sys.argv[3], "c")

        calculate_roots(coeff_a, coeff_b, coeff_c)         

def get_coeff_a():
    try:
        coeff_a = float(input("Enter coefficient A: "))
        return coeff_a
    except ValueError:
        print(f"Incorrect coeffinient A entered. Please try again" + '\n')
        while True:
            try:
                coeff_a = float(input(f"Enter coefficient A: "))
                return coeff_a
            except ValueError:
                print(f"Incorrect coeffinient A entered. Please try again" + '\n')
    

def get_coeff_b():
    try:
        coeff_b = float(input("Enter coefficient B: "))
        return coeff_b
    except ValueError:
        print(f"Incorrect coeffinient B entered. Please try again" + '\n')
        while True:
            try:
                coeff_b = float(input(f"Enter coefficient B: "))
                return coeff_b
            except ValueError:
                print(f"Incorrect coeffinient B entered. Please try again" + '\n')


def get_coeff_c():
    try:
        coeff_c = float(input("Enter coefficient C: "))
        return coeff_c
    except ValueError:
        print(f"Incorrect coeffinient C entered. Please try again" + '\n')
        while True:
            try:
                coeff_c = float(input(f"Enter coefficient C: "))
                return coeff_c
            except ValueError:
                print(f"Incorrect coeffinient C entered. Please try again" + '\n')

def Check_correctness_coefficient_from_arg(coeff, coeff_name):
    try:
        coeff = float(coeff)
        return coeff
    except ValueError:
        print(f"Incorrect coeffinient {coeff_name} entered. Please try again" + '\n')
        while True:
            try:
                coeff = float(input(f"Enter coefficient {coeff_name}: "))
                return coeff
            except ValueError:
                print(f"Incorrect coeffinient {coeff_name} entered. Please try again" + '\n')


def calculate_roots(coeff_a, coeff_b, coeff_c):
    print('\n' + "entered coefficiients:" + '\n')
    print(f"coefficient A: {coeff_a}")
    print(f"coefficient B: {coeff_b}")
    print(f"coefficient C: {coeff_c}" + '\n')

    roots = []

    discriminant = coeff_b**2 - 4*coeff_a*coeff_c
    if discriminant < 0:
        print('No roots found')
        return
    
    else:
        root1 = (-coeff_b + math.sqrt(discriminant)) / (2 * coeff_a)
        roots.append(root1)
        root2 = (-coeff_b - math.sqrt(discriminant)) / (2 * coeff_a)

        if root2 != root1:
            roots.append(root2)
    print(f"finded roots --- {roots}")

IsQuantityArgsCorrect()