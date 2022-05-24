def show_format(table):
    keys = table[0].keys()
    values = table[0].values()
    for key in keys:
        print("{:<8}".format(key), end=" ")
        # print(key, end=" | ")
    print()
    for i in range(0, len(table)):
        values = table[i].values()
        for value in values:
            print("{:<8}".format(value), end=" ")
        print()
    return table


if __name__ == '__main__':
    show_format([{"id": 1, "name": "Lucas", "age": 22}, {"id": 2, "name": "Gabi", "age": 22}, {"id": 3, "name": "Gabi", "age": 22}])
