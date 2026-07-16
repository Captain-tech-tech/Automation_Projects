
# the json schema contain the rules, while DataTypeValidator.py contains the logic for checking those rules

import pandas as pd 
from utils.logger import logger

# schema is for expected column data types and rules
def validateDatatype(df :pd.DataFrame ,schema : dict)-> tuple[bool,list[str]]:  # tuple[bool,list[str]]  it tells the return type

    errors = []  # initially we assume there are zero errors

    column_schema = schema["columns"]


    # column_name  is temporary name given to current DataFrame column
    # column_rules stores all the validation rules for the current column 
    # .items grab key(column_name) and its value(expected_type) at the same time
    # this loops through the content of column_schema
    for column_name, column_rules in column_schema.items():

        # checking whether the column exists or not
        if column_name not in df.columns:
            error_message = (
                f"missing columns : '{column_name}'"
            )
            errors.append(error_message)
            logger.error(error_message)

            # if the column does not exist, simply move to the next column
            continue 

        column = df[column_name]

        expected_type = column_rules["type"]

        # now validate integer columns
        if expected_type == "integer":            
            if not pd.api.types.is_integer_dtype(column):
                error_message = (
                    f"column '{column_name}'"
                    f"must be an integer"
                )

                logger.error(error_message)
                errors.append(error_message)

        # validate float column
        elif expected_type == "float":
            if not pd.api.types.is_float_dtype(column):
                error_message = (
                    f"column '{column_name}'"
                    f"must be float"
                )
                
                logger.error(error_message)
                errors.append(error_message)

        # validating string column
        elif expected_type == 'string':
            if not pd.api.types.is_string_dtype(column):
                error_message = (
                    f"column '{column_name}'"
                    f"must be a string"
                )

                logger.error(error_message)
                errors.append(error_message)

        # detecting unsupported schema type
        else :
            error_message = (
                f"Unsupported datatype : '{expected_type}'"
                f"for column '{column_name}'"
            )

            logger.error(error_message)
            errors.append(error_message)

    if errors:
        
        logger.error(
            f"DataType validation failed with "
            f"{len(errors)} error(s)"
        )

        return False,errors 
    
    logger.info("Datatype validation successfully done!")
    return True, []


# this above function loops through every rule in the schema, check whether the required column exist 
# and has the correct datatype, collect all problems, log the result, and return a clear success 
# or failure result




