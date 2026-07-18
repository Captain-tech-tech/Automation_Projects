# domain validation determine whether a value is valid
# statistical outlier detection determine whether a value is unusual -->  they are not the same


import pandas as pd
from utils.logger import logger 

def detect_iqr_outliers(df: pd.DataFrame,column: str,multiplier: float = 1.5) -> pd.DataFrame:

    try:
        if column not in df.columns:
            raise ValueError(f"Column '{column}' does not exist")
    
    except Exception as e:
        print(e)
    
    else:    
        try:
            if not pd.api.types.is_numeric_dtype(df[column]):
                raise TypeError(
                    f"Column '{column}' must be numeric."
                )
        except Exception as e:
            print(e)
        else:
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)

            iqr = q3 - q1

            lower_b = q1 - multiplier * iqr
            upper_b = q3 + multiplier * iqr

            outlier_mask = ((df[column] < lower_b) | (df[column] > upper_b))

            outliers = df[outlier_mask]

            logger.info(
                f"{len(outliers)} outlier(s) detected "
                f"in column '{column}'."
            )
            
            return len(outliers)









