from utils.file_handler import load_dataset
from utils.logger import logger
import pandas as pd
import json 


from validator.DataTypeValidator import validateDatatype

def main():
    
    path = input("Enter the path of the file: ")
    dataframe = load_dataset(path)


    print(
        "Enter (1) for student file!",
        "\nEnter (2) for sales file",
        "\nEnter (3) for employee file",
        "\nEnter (4), if it is any other type of file", end='\t'
    )
    try:
        n = int(input(" : "))
    except ValueError:
        print("please enter a number")
        logger.error("User entered a non-numeric schema choice")
        main()
    else:    
        if (n==1):
            schema_path = "schema/student.json"
            
        elif(n==2):
            schema_path = "schema/customer_products_schema.json"
           
        elif(n==3):
            schema_path = "schema/employee.json"
            
        elif (n==4):
            print("Sorry, we can't processed it further, as this file data is not supported!")
            logger.error("This type of file can't be validate!")
            return 
        else:
            print("Invalid choice")
            logger.error(
                f"Invalid schema type is selected '{n}'"
            )  
            return
    finally :
            with open(schema_path,"r") as f:
                schema = json.load(f)
                is_valid,error = validateDatatype(dataframe,schema)
  





main()


print("Rest of the code")
