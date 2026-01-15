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
    
    def insert_into_row(self, table_name, row_data):
        print(f"Inserting into table...: {table_name} data: {row_data}")

        #read table
        table =  self.storage.read_table(table_name)
        print(f"Table data: {table}")

        is_valid, error = self.schema_manager.validate_row_data(table, row_data)
        if not is_valid:
            return f"Data does not conform to table {table} schema + {error}"

        #insert the row
        row_index = len(table["rows"])
        table["rows"].append(row_data)

        #update indexes
        self._update_indexes(table, row_data, row_index)
        print(f"update indexes done...")
        # save to -- storage
        self.storage.write_table(table_name, table)
        

        return f"Data inserted into table {table_name} successfully"



    def _update_indexes(self, table, row_data, row_index):
        print(table["indexes"])
        for column_name in table["indexes"]:
            if column_name in row_data:
                value = row_data[column_name]
                table["indexes"][column_name]["map"][value] = row_index

