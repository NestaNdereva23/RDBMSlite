import os
import json

class Storage:
    def __init__(self, db_directory="/home/knuclezz/Documents/rdbmslite/database"):
        self.db_directory = db_directory
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)

    def table_exists(self, table_name):
        return os.path.join(self.db_directory, f"{table_name}.json")

    def storage_exists(self, table_name):
        return os.path.exists(self.table_path_exists(table_name))

    def create_table(self, table_name, data):
        #check if table exists
        path = self.table_path_exists(table_name)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)


