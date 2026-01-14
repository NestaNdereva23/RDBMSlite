import sys
import core
from compiler import tokenize, parser

def start_prompt():
    print("Welcome to the RDBMS Lite")
    while True:
        s = input("RDBMS Lite> ").strip().lower()
        if s == "":
            continue
        elif s in ('exit', 'quit'):
            print("Exiting RDBMS Lite.")
            sys.exit(0)
        else:
            execute_statement(s)

def execute_statement(s: str):
    print(f"DB statement before tokenizing: {s}")
    t = tokenize.tokenizer(s)
    parser.parse(t)

