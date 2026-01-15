class SchemaManager:

    @staticmethod
    def create_schema(table_name, columns):
        schema = {
            "table_name": table_name,
            "schema": {
                "columns":{}
            },
            "rows":[],
            "indexes":{}
        }

        #process the columns (name, type, constraints)
        for i in range(0, len(columns), 3):
            col_name = columns[i]
            col_type = columns[i+1].upper()
            constraints = columns[i+2] if i+2 < len(columns) else []

            col_definition = {
                "type": col_type,
                "nullable": "NOT NULL" not in constraints
            }

            #Constraints flags
            if "PRIMARY KEY" in constraints:
                col_definition["primary_key"] = True
                col_definition["unique"] = True
                col_definition["nullable"] = False

                #create index for primary key
                schema["indexes"][col_name] = {
                    "type": "hash",
                    "map": {}
                }

            if "UNIQUE" in constraints and "PRIMARY KEY" not in constraints:
                col_definition["unique"] = True

                #create index for unique constraint
                schema["indexes"][col_name] = {
                    "type": "hash",
                    "map": {}
                }

            schema["schema"]["columns"][col_name] = col_definition
        
        return schema

    @staticmethod
    def validate_row_data(schema, row_data):
        # {'id': '1', 'email': "'user@example.com')"}
        columns = schema["schema"]["columns"]

        for col_name, col_definition in columns.items():
            if not col_name.get('nullable', True) and col_name not in row_data:
                return f'Column {col_name} cannot be null'

            if col_name in row_data:
                value = row_data[col_name]
                expected_type = col_definition["type"]

                #check type

        return True, None
