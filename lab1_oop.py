import math
import sys

REQUIRED_NUMBER_OF_ARGUMENTS = 4
MIN_NUMBER_OF_ARGUMENTS = 1

class Quadratic_Equation:

    def __init__(self, coeff_a: float = 0, coeff_b: float = 0, coeff_c: float = 0):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c
    
    def Calculate_roots(self):
        roots = []

        discriminant = self.__coeff_b**2 - 4*self.__coeff_a*self.__coeff_c
        if discriminant < 0:
            print('No roots found')
            exit()
        
        else:
            root1 = (-self.__coeff_b + math.sqrt(discriminant)) / (2 * self.__coeff_a)
            roots.append(root1)
            root2 = (-self.__coeff_b - math.sqrt(discriminant)) / (2 * self.__coeff_a)

            if root2 != root1:
                roots.append(root2)
        print(f"finded roots --- {roots}")
pass


def From_User_Input_A():
    try:
        coeff_a = float(input("Enter coefficient A: "))
        return coeff_a
    except ValueError:
        print("Incorrect coeffinient A entered. Please try again" + '\n')
        while True:
            try:
                coeff_a = float(input("Enter coefficient A: "))
                return coeff_a
            except ValueError:
                print("Incorrect coeffinient A entered. Please try again" + '\n')
        

def From_User_Input_B():
    try:
        coeff_b = float(input("Enter coefficient B: "))
        return coeff_b
    except ValueError:
        print("Incorrect coeffinient B entered. Please try again" + '\n')
        while True:
            try:
                coeff_b = float(input("Enter coefficient B: "))
                return coeff_b
            except ValueError:
                print("Incorrect coeffinient B entered. Please try again" + '\n')
        
def From_User_Input_C():
    try:
        coeff_с = float(input("Enter coefficient С: "))
        return coeff_с
    except ValueError:
        print("Incorrect coeffinient С entered. Please try again" + '\n')
        while True:
            try:
                coeff_с = float(input("Enter coefficient С: "))
                return coeff_с
            except ValueError:
                print("Incorrect coeffinient С entered. Please try again" + '\n')
    
def Check_correctness_coefficient_from_arg(coeff, coeff_name):
    try:
        coeff = float(coeff)
        return coeff
    except ValueError:
        print("Incorrect coeffinient {coeff_name} entered. Please try again" + '\n')
    while True:
        try:
            coeff = float(input(f"Enter coefficient {coeff_name}: "))
            return coeff
        except ValueError:
            print(f"Incorrect coeffinient {coeff_name} entered. Please try again" + '\n')
        
   
def IsQuantityArgsCorrect():
    if len(sys.argv) > REQUIRED_NUMBER_OF_ARGUMENTS:
        print("Too many arguments entered, please try again '\n'")
        equation = Quadratic_Equation(From_User_Input_A(), From_User_Input_B(), From_User_Input_C())
        equation.Calculate_roots()

    elif len(sys.argv) < REQUIRED_NUMBER_OF_ARGUMENTS:
        print("Too few arguments entered, please try again '\n'")
        equation = Quadratic_Equation(From_User_Input_A(), From_User_Input_B(), From_User_Input_C())
        equation.Calculate_roots()
        
    else:
        coeff_a = Check_correctness_coefficient_from_arg(sys.argv[1], "a")
        coeff_b = Check_correctness_coefficient_from_arg(sys.argv[2], "b")
        coeff_c = Check_correctness_coefficient_from_arg(sys.argv[3], "c")

        equation = Quadratic_Equation(coeff_a, coeff_b, coeff_c)
        equation.Calculate_roots()

IsQuantityArgsCorrect()


