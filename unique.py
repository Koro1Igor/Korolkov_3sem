class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            val = item.lower() if self.ignore_case and isinstance(item, str) else item
            if val not in self.seen:
                self.seen.add(val)
                return item
        raise StopIteration


if __name__ == '__main__':
    
    user_input = input("Введите элементы через пробел: ")
    data = user_input.split() 

    ignore_case_input = input("Игнорировать регистр? (y/n): ").lower()
    ignore_case = ignore_case_input == 'y'

    unique_iter = Unique(data, ignore_case=ignore_case)

    print("Уникальные элементы:")
    for item in unique_iter:
        print(item)

