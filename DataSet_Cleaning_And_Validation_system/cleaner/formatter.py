import pandas as pd
from utils.logger import logger

def trim_spaces(
    df: pd.DataFrame,
    columns: None
) -> pd.DataFrame:

    if columns is None:
        columns = df.columns

    df = df.copy()

    fixed_columns = set()

    for column in columns:
        if column in df.columns:
            if df[column].dtypes == "object":
                df[column] = df[column].str.strip()
                fixed_columns.add(column)
    
        
    logger.info(
        "Spaces trimmed successfully."
    )

    columns_fixed = len(fixed_columns)

    return df,columns_fixed


def convert_to_uppercase(
    df: pd.DataFrame,
    columns: list[str]
) -> pd.DataFrame:

    df = df.copy()

    for column in columns:

        if column not in df.columns:

            logger.warning(
                f"Column '{column}' does not exist."
            )

            continue

        df[column] = (
            df[column]
            .astype("string")
            .str.upper()
        )

    return df


def convert_to_lowercase(
    df: pd.DataFrame,
    columns: list[str]
) -> pd.DataFrame:

    df = df.copy()

    for column in columns:

        if column not in df.columns:

            logger.warning(
                f"Column '{column}' does not exist."
            )

            continue

        df[column] = (
            df[column]
            .astype("string")
            .str.lower()
        )

    return df


def format_date(
    df: pd.DataFrame,
    column: str,
    date_format: str = "%Y-%m-%d"
) -> pd.DataFrame:

    df = df.copy()

    if column not in df.columns:

        logger.warning(
            f"Column '{column}' does not exist."
        )

        return df

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    ).dt.strftime(date_format)

    return df


def format_phone_numbers(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:

    df = df.copy()

    if column not in df.columns:

        logger.warning(
            f"Column '{column}' does not exist."
        )

        return df

    df[column] = (
        df[column]
        .astype("string")
        .str.replace(
            r"\D",
            "",
            regex=True
        )
    )

    return df


def format_currency(
    df: pd.DataFrame,
    column: str,
    currency_symbol: str = "$"
) -> pd.DataFrame:

    df = df.copy()

    if column not in df.columns:

        logger.warning(
            f"Column '{column}' does not exist."
        )

        return df

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    df[column] = (
        df[column]
        .map(
            lambda value:
            f"{currency_symbol}{value:,.2f}"
            if pd.notna(value)
            else value
        )
    )

    return df



# format_phone_numbers, format_currency, convert_to_lowercase, format_date   --> these functions are added for future use 
