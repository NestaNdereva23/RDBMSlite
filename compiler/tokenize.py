def tokenizer(statement: str):
    tokens = []

    statement = statement.strip()
    tokens = statement.split()

    print(f"Statement after tokenizing: {tokens}")
    print(type(tokens))

    return tokens