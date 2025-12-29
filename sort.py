if __name__ == '__main__':
    user_input = input("Введите числа через пробел: ")
    
    data = [int(x) for x in user_input.split()]

    result = sorted(data, key=abs, reverse=True)
    print("Сортировка по модулю без lambda:", result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("Сортировка по модулю с lambda:", result_with_lambda)

