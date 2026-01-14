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

    executor = Executor()
    return executor.create_table_command(table_name, columns)



