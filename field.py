def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            val = item.get(args[0])
            if val is not None:
                yield val
        else:
            d = {k: item.get(k) for k in args if item.get(k) is not None}
            if d:
                yield d

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
