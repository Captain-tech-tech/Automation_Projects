import pandas as pd
from utils.logger import logger


def detect_missing_values(df = pd.DataFrame) -> pd.DataFrame:

    missing_rows = df[df.isnull().any(axis=1)]

    if missing_rows.empty:
        logger.info("No missing values detected!")
    else :
        logger.warning(
            f"Missing values detected in "
            f"{len(missing_rows)} row(s)"
        )
    return missing_rows

def count_missing_values(df : pd.DataFrame)-> pd.Series:
    missing_counts = df.isnull().sum()

    total_missing = missing_counts.sum()

    if total_missing == 0:
        logger.info("No missing values found")
    else:
        logger.warning(
            f"Total missing values found "
            f"{total_missing}"
        )
    return missing_counts



def fill_numeric_missing_values(df : pd.DataFrame,strategy : str = "median") -> pd.DataFrame:

    df = df.copy()
    missing_before = df.isna().sum().sum()

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:
        missing_count = df[column].isnull().sum()  # .isnull().sum() counts the number of missing (NaN) values in each column of a Pandas DataFrame

        if missing_count == 0:
            continue 

        if strategy == "mean":
            replacement_value = (df[column].mean())
        elif strategy == "median":
            replacement_value = (df[column].median())
        elif strategy == "zero":
            replacement_value = 0
        else :
            raise ValueError(
                f"Unsupported numeric strategy"
                f"{strategy}"
            )
        
        df[column] = df[column].fillna(replacement_value)

        logger.info(
            f"filled {missing_count} missing value(s)"
            f" in '{column}' using '{strategy}'"
        )

    missing_after = df.isna().sum().sum()

    filled_values = (missing_before - missing_after)

    return df,filled_values 

def fill_categorical_missing_values(df : pd.DataFrame, strategy : str = "unknown") -> pd.DataFrame:
    df = df.copy()

    categorical_columns = df.select_dtypes(
        include=["object","string","category"]
    ).columns

    for column in categorical_columns:
        missing_count = df[column].isnull().sum()

        if missing_count == 0:
            continue
        if strategy == "unknown":
            replacement_value = "Unknown"
        elif strategy == "mode":
            mode_values = df[column].mode()

            if mode_values.empty:
                replacement_value = "Unknown"
            else:
                replacement_value = mode_values.iloc[0]
        else:
            raise ValueError(
                f"Unsupported categorical strategy "
                f"{strategy}"
            )
        
        df[column] = df[column].fillna(replacement_value)

        logger.info(
            f"filled {missing_count} missing value(s) "
            f"'{column}' using '{strategy}'"
        )
    return df,missing_count







# detect_missing_values()      only detect, where are the missing values 
# count_missing_values()       only count, how many missing values 
# fill_numeric_missing_values()        only clean numeric column, tell how numeric values be filled
# fill_categorical_missing_values()        only clean categorical columns, tell how text/category values be filled
# handle_missing_values()         coordinate the complete process, run the complete missing value cleaning process

