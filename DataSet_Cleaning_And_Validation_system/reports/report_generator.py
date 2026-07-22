def generate_text_report(report,output_path):
    report_text = f"""
==================================================
              DATA CLEANING REPORT
==================================================

Rows Before              : {report.rows_before:,}
Rows After               : {report.rows_after:,}

Duplicate rows removed   : {report.duplicates_removed:,}
Duplicate ids removed    : {report.duplicate_ids_removed:,}
Missing values filled    : {report.missing_values_filled:,}
Outliers found           : {report.outliers_found:,}
Columns fixed            : {report.columns_fixed:,}

Input file               : f{report.input_file}
Ouput file               : f{report.output_file}

Execution time           : {report.execution_time:.2f} seconds

Status                   : {report.status}

==================================================
"""

    with open(output_path,"w",encoding="utf-8") as file:
        file.write(report_text)



