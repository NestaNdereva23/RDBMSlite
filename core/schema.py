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
            if "primary_key" in constraints:
                col_definition["primary_key"] = True
                col_definition["unique"] = True
                col_definition["nullable"] = False

                #create index for primary key
                schema["indexes"][col_name] = {
                    "type": "hash",
                    "map": {}
                }

            if "unique" in constraints and "primary_key" not in constraints:
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
        # print(f"Validating row data: {row_data} against schema columns: {columns}")

        converted_data = {}

        for col_name, col_definition in columns.items():
            if not col_definition.get('nullable', True) and col_name not in row_data:
                return False, f'Column {col_name} cannot be null'

            if col_name in row_data:
                value = row_data[col_name]
                expected_type = col_definition["type"]
                # print(f"value: {value}, expected_type: {expected_type}")


                #convert then check type
                converted_value = SchemaManager.convert_value(value, expected_type)
                if converted_value is None and value is not None:
                    return False, f"Column {col_name} must be of type: {expected_type}"
                
                
                #check type --->eg INT, TEXT
                is_valid = SchemaManager._check_type(converted_value, expected_type)
                if not is_valid:
                    return False, f"Column {col_name} must be of type: {expected_type}"
                
                #store converted value
                converted_data[col_name] = converted_value
            else:
                converted_data[col_name] = None

                # print(f"Column {col_name} with value {value} passed type check as {expected_type}")
        # print("All columns passed validation")
        return True, None

    @staticmethod
    def _check_type(value, expected_type):
        #supported values -->INT, TEXT, BOOLEAN
        if expected_type == "INT":
            return isinstance(value, int)
        elif expected_type == "TEXT":
            return isinstance(value, str)
        elif expected_type == "BOOLEAN":
            return isinstance(value, bool)
        return True
    
    #convert row values to proper types based on schema
    @staticmethod
    def convert_value(value, expected_type):
        """Convert string value to the expected type"""
        try:
            if expected_type == "INT":
                return int(value)
            elif expected_type == "TEXT":
                return str(value)
            elif expected_type == "BOOLEAN":
                if isinstance(value, bool):
                    return value
                # Handle string boolean values
                if value.lower() in ('true', '1', 'yes'):
                    return True
                elif value.lower() in ('false', '0', 'no'):
                    return False
                else:
                    raise ValueError(f"Cannot convert '{value}' to BOOLEAN")
            return value
        except (ValueError, AttributeError) as e:
            return None  # Return None if conversion fails