import tools as t


def create_table(name, columns):
    keys = dict.fromkeys(columns, None)
    name = [keys]
    return name


def insert(table, values):
    last_id = table[len(table) - 1]['id']
    items = values.items()
    keys = values.keys()

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


def select(columns, From):
    formatted_columns = columns.replace(" ", "")

    if formatted_columns == '*':
        return From
    elif formatted_columns == 'count':
        return len(From)
    else:
        request_columns = formatted_columns.split(',')
        result = []
        for f in range(0, len(From)):
            items = From[f].items()
            for i in range(0, len(request_columns)):
                for k, v in items:
                    if request_columns[i] == k:
                        if i == 0:
                            result.append({k: v})
                        else:
                            result[f][k] = v

    return result


def From(table, where=None):  # verificar como colocar "from"
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


def update(table, set={}, where=None):
    items = set.items()
    if where is None:
        for i in range(0, len(table)):
            for key, value in items:
                table[i][key] = value
    else:
        update_rows = select('*', From(table, where))
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
        delete_rows = select('*', From(table, where))
        for row in delete_rows:
            if row in table:
                table.remove(row)
    # return [i for i in table if i not in select(table, where)]
    return table


# testes
if __name__ == '__main__':
    students = create_table("students", ["id", "name", "age", "house"])
    insert(students, {"name": "Lucas", "age": 22, "house": "Sonserina"})
    insert(students, {'name': 'Gabi', 'age': 22, 'house': 'Lufa-Lufa'})
    insert(students, {'name': 'Erico', 'age': 41, 'house': 'Grifinória'})
    insert(students, {'name': 'Beth', 'age': 65, 'house': 'Corvinal'})
    t.show_format(students)

    update(students, set={'name': 'Bravim'}, where={'age': 65})
    print()
    t.show_format(students)

    delete(students, where={'id': 3})
    print()
    t.show_format(students)

    insert(students, values={'name': 'Rony', 'age': 7, 'house': 'Grifinória'})
    print()
    t.show_format(students)

    query = select('name, house', From(students, where={'age': 22}))
    print()
    t.show_format(query)
