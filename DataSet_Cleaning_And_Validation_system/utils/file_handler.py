# this file take the .xlsx or csv file and return the DataFrame
# this file follows Single Reponsibilty Principle (SRP)


class InvalidPathError(Exception):
    ...

class InvalidFileError(Exception):
    ...

import pandas as pd
from pathlib import Path 
from utils.logger import logger 

# checking whether the path is correct or not and also checking whether the file format is  correct or not
# the function also return a DataFrame

logger.info("File validation started!")

def load_dataset(f_path):

    # convert the input into path object
    file_path = Path(f_path)

    # checking whether file path exist or not and raising self defined exception
    try:
        if file_path.is_file():
            print("Successful, the file exists!")
        else :
            raise InvalidPathError("Invalid path is entered!")
    except Exception as e:
        print("ErrorType :",e)
        logger.warning("File path does not exists!")
    else:

        logger.info("File path exists!")
        # nested exception is used for checking file format
        try:
            if file_path.suffix.lower() == '.csv':
                print("It is a csv file!")
                q = 1
                logger.info("csv file is loaded successfully!")
            elif file_path.suffix.lower() == '.xlsx':
                print("It is a xlsx file")
                q = 2
                logger.info("xlsx file is loaded successfully!")
            else:
                raise InvalidFileError("Unsupported : This file is neither a csv nor a xlsx file!")
        except Exception as e:
            print("ErrorType :",e)
            logger.warning("Invalid file format for loading!")
        
        # if file is valid, converting it into DataFrame 
        else :
            if q == 1:
                df = pd.read_csv(f_path)
                logger.info("File successfully converted into DataFrame!")
                return df 
            elif q == 2:
                df = pd.read_excel(f_path)
                logger.info("File successfully converted into DataFrame!")
                return df 

        


