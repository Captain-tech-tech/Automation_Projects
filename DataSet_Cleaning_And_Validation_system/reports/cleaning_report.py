from dataclasses import dataclass, field
from typing import Dict
import time

@dataclass
class CleaningReport:

    rows_before: int = 0
    rows_after: int = 0

    duplicates_removed: int = 0
    duplicate_ids_removed: int = 0

    missing_values_filled: int = 0
    outliers_found: int = 0

    columns_fixed: int = 0

    execution_time: float = 0.0

    input_file: str = ""
    output_file: str = ""

    status: str = "SUCCESS"


        