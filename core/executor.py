import json
from core.storage import Storage
from core.schema import SchemaManager

class Executor:
    def __init__(self):
        self.storage = Storage(db_directory="/home/knuclezz/Documents/rdbmslite/database")
        self.schema_manager = SchemaManager()

    def create_table_command(self, table_name, columns):
        print(f"Creating table...: {table_name}")

        #check if table exists
        if self.storage.table_exists(table_name):
            print(f"Table {table_name} already exists")

        #build the schema
        table_structure = self.schema_manager.create_schema(table_name, columns)

        #save to storage
        self.storage.create_table(table_name, table_structure)

        return f"Table {table_name} created successfully"
    
    def insert_into_command(self, table_name, row_data):
        print(f"Inserting into table...: {table_name} data: {row_data}")

            
        is_valid, error = self.schema_manager.validate_row_data(table_name, row_data)
        if not is_valid:
            return f"Data does not conform to table {table_name} schema + {error}"

        #insert the data
        self.storage.insert_into_table(table_name, row_data)

        return f"Data inserted into table {table_name} successfully"





