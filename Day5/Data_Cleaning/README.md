# Day 5 – Task 1: Data Cleaning

## Files
- `Task1.py` — Python script that performs the cleaning.
- `sales_data.csv` — Small practice dataset containing missing values, inconsistent text, and a duplicate row.
- `clean_data.csv` — Generated automatically when `Task1.py` runs.

## Run in VS Code
1. Extract the ZIP file.
2. Open the `Day5` folder (or the `Data_Cleaning` folder) in VS Code.
3. Open the terminal in `Data_Cleaning`.
4. Install pandas if needed: `python -m pip install pandas`
5. Run: `python Task1.py`

The script saves `clean_data.csv` in the same folder as `Task1.py`.

## Cleaning decisions
- `Age`: fill missing values with the median; it is numeric and the median is less sensitive to outliers.
- `Sales`: fill missing values with the median for the same reason.
- `Customer`, `City`, `Order_Date`, and `Category`: leave missing values as missing if present, because their correct values cannot be safely inferred. The remaining missing values are therefore visible/flagged in the summary.
- `Order_ID`: retain as an identifier; do not invent an ID if one is missing.
- Text columns are trimmed and converted to title case.
- `Age` and `Sales` are converted to numeric values; `Order_Date` is converted to a date.
- Exact duplicate rows are removed.
- Sales outliers are detected using the IQR rule and retained for review rather than automatically deleted.

This is a small practice dataset. The assignment's example counts (1480, 1470, etc.) are illustrative; your results depend on the dataset used.
