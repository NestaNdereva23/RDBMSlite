import re
import sys
import tokenize
from core.executor import Executor



def parse(tokens: list):
    #identify the command >. token[0] then process
    #supported commands CREATE, INSERT, SELECT

    command = tokens[0].upper()

    if command == "CREATE":
        return parseCreate(tokens)
    
    if command == "INSERT":
        return parseInsert(tokens)

    else:
        print("Unknown command")
        sys.exit(0)


def parseCreate(tokens: list):
    '''CREATE TABLE table_name (
    column1 datatype [constraints],
    column2 datatype [constraints],
    column3 datatype [constraints],
    ...
    );

    supported syntax >> CREATE TABLE users (id INT, email TEXT);
    TABLE == token[1] -->pos 2
    () --> column definitions
    '''
    table_name = tokens[2]

    full_string = " ".join(tokens)
    columnsPart = full_string.split('(')[1].split(')')[0]

    print(f" columnsParts: {columnsPart}")
    columnDefinitions = [col.strip() for col in columnsPart.split(',')]

    print(table_name)
    print(columnDefinitions)
    columns = []
    for definition in columnDefinitions:
        parts = definition.split(' ')
        columnName = parts[0]
        columnType = parts[1]
        constraints = parts[2:]

        columns.append(columnName)
        columns.append(columnType)
        columns.append(constraints)

    print(f"columns: {columns} and len: {len(columns)}")
    executor = Executor()
    return executor.create_table_command(table_name, columns)

def parseInsert(tokens: list):
    '''INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);

    supported syntax >> INSERT INTO users (id, email) VALUES (1, 'user@example.com');
    '''
    table_name = tokens[2]

    # Extract column names
    columnsPart = " ".join(tokens).split('(')[1].split(')')[0]
    columnNames = [col.strip() for col in columnsPart.split(',')]

    # Extract values
    valuesPart = " ".join(tokens).lower().split('values')[1].strip()
    valuesPart = valuesPart[1:-1]  # Remove parentheses
    values = [val.strip() for val in valuesPart.split(',')]

    row_data = {} # hold col_names and values
    for i in range(len(columnNames)):
        row_data[columnNames[i]] = values[i]


    executor = Executor()
    return executor.insert_into_row(table_name, row_data)
