import os
import json

class Storage:
    def __init__(self, db_directory="/home/knuclezz/Documents/rdbmslite/database"):
        self.db_directory = db_directory
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)

    def get_table_path(self, table_name):
        table_path = os.path.join(self.db_directory, f"{table_name}.json")
        return table_path

    def table_exists(self, table_name):
        return os.path.exists(self.get_table_path(table_name))

    def create_table(self, table_name, data):
        #check if table exists
        path = self.get_table_path(table_name)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def read_table(self, table_name):
        # check if table exists
        if not self.table_exists(table_name):
            return FileNotFoundError(f'Table {table_name} does not exist')

        # if exists read data from table
        table_path = os.path.join(self.db_directory, f"{table_name}.json")
        with open(table_path, "r") as f:
            return json.load(f)

    def write_table(self, table_name, table_data):
        path = self.get_table_path(table_name)

        with open(path, "w") as f:
            json.dump(table_data, f, indent=2)



