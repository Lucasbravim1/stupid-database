import tools as t


def create_table(name, columns):
    keys = dict.fromkeys(columns, None)
    name = [keys]
    return name


def insert(table, column_values):
    last_id = table[len(table) - 1]['id']
    items = column_values.items()
    keys = column_values.keys()

    if last_id is None:  # primeira linha
        table[0]['id'] = 1
        # faz o insert
        for key, value in items:
            table[0][key] = value
    # demais execucoes
    else:
        last_id += 1  # chave primária --> sequencial
        id_column = {'id': last_id}
        new_row = dict.fromkeys(keys, None)
        for key, value in items:  # atribui os valores passados
            new_row[key] = value
        id_column.update(new_row)
        table.append(id_column)

    return table


def select(table, where=None):
    if where is None:
        return table
    else:
        items = where.items()
        result = []
        for i in range(0, len(table)):
            for key, value in items:
                if table[i][key] == value:
                    result.append(table[i])
        return result


def update(table, values, where=None):
    items = values.items()
    if where is None:
        for i in range(0, len(table)):
            for key, value in items:
                table[i][key] = value
    else:
        update_rows = select(table, where)
        id = update_rows[0]['id']
        for j in range(0, len(update_rows)):
            for key, value in items:
                table[id - 1][key] = value
                id += 1
    return table


def delete(table, where=None):
    if where is None:
        table.clear()
    else:
        delete_rows = select(table, where)
        for row in delete_rows:
            if row in table:
                table.remove(row)
    # return [i for i in table if i not in select(table, where)]
    return table


if __name__ == '__main__':
    students = create_table("students", ["id", "name", "age", "house"])
    insert(students, {"name": "Lucas", "age": 22, "house": "Sonserina"})
    insert(students, {'name': 'gabi', 'age': 22, 'house': 'grifinoria'})
    insert(students, {'name': 'erico', 'age': 39, 'house': 'gsd'})
    insert(students, {'name': 'beth', 'age': 55, 'house': 'dasdsa'})
    update(students, {"name": "Harry"}, {"age": 22})
    delete(students, {'age': 55})
    t.show_format(students)
