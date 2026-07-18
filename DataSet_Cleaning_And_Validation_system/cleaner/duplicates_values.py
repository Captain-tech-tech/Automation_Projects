import pandas as pd
from utils.logger import logger 

# detecting duplicate rows in the dataframe
def detect_duplicates(df : pd.DataFrame) -> pd.DataFrame:
    
    # this line is use to select only the rows where the condition is true
    duplicate_rows = df[df.duplicated()]    # df.duplicated()  returns a boolean series 

    if duplicate_rows.empty:      # or  if duplicate_rows.empty:     if zero duplicates, it return True
        logger.info("No duplicate values found!")

    else:
        logger.warning(f" '{len(duplicate_rows)}' duplicate rows were found!")

    
    return duplicate_rows



# function to remove duplicate values
# this function will be called only, if duplicate values detected through the above function
def remove_duplicates(df : pd.DataFrame,report) -> pd.DataFrame:

    original_row_count = len(df)

    cleaned_df = df.drop_duplicates()

    removed_row_count =  (original_row_count - len(cleaned_df))

    report.duplicates_removed += removed_row_count

    logger.info(f"'{removed_row_count}' duplicate row(s) removed successfully!")

    return cleaned_df


def remove_duplicate_ids(df : pd.DataFrame, report, id_column : str = "id") -> pd.DataFrame:
    # check whether the id column exist or not

    try:
        if id_column not in df.columns:
            logger.error("id column does not exists!")
            raise ValueError(f"ID column 'id' does not exist!")
    except Exception as e:
        print(e)
    else:
        # detecting duplicate ids
        duplicate_id_rows = df[df[id_column].duplicated(keep=False)]

        # logging duplicate ids
        if not  duplicate_id_rows.empty:
            logger.warning(f"{len(duplicate_id_rows)} rows contain duplicate ids")
        else :
            return df

        # removing duplicate ids
        cleaned_df = df.drop_duplicates(subset=[id_column],keep="first")

        # calculate number of removed rows
        removed_rows = (len(df) - len(cleaned_df))
        logger.info(f"{removed_rows} duplicate id record(s) removed successfully")

        report.duplicate_ids_removed = len(df) - len(cleaned_df)

        return cleaned_df


       






