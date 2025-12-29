from rectangle import Rectangle
from circle import Circle
from square import Square

from colorama import Fore, Style, init

def main():
    init(autoreset=True)

    NUMBER_OF_VARIANT = 15

    rect = Rectangle(NUMBER_OF_VARIANT, NUMBER_OF_VARIANT, "синий")
    circle = Circle(NUMBER_OF_VARIANT, "зеленый")
    square = Square(NUMBER_OF_VARIANT, "красный")

    print(Fore.BLUE + str(rect))
    print(Fore.GREEN + str(circle))
    print(Fore.RED + str(square))

if __name__ == "__main__":
    main()
