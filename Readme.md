# CSV File Comparator and Updater

This tool is designed to compare the first columns of two CSV files, identify missing rows based on specific naming conventions, and append the missing rows to the second file. It provides a graphical interface for selecting files and saving the updated file, making it a practical utility for managing data consistency in various use cases.

While this tool can be applied to any CSV comparison task, it was initially created to manage and update variable definitions in SCADA projects, such as those in Zenon, where naming conventions often follow specific prefixes or IDs.

## Features

- **Flexible File Selection**: Select two CSV files for comparison using an intuitive graphical interface.
- **ID-based Matching**: Identifies missing rows by analyzing an ID, defined as the first three characters of the variable names in the first column.
- **Dynamic Updates**: Appends missing rows from the first file to the second file, adapting the ID prefix to match the second file’s format.
- **Case-Insensitive Comparison**: Ensures variable matching is not affected by letter casing.
- **Save Updated File**: Provides an option to save the updated file with appended rows to a location of your choice.

## Prerequisites

- Python 3.6 or higher
- Libraries: `pandas`, `tkinter`, `chardet`

Install the required libraries using pip:

```bash
pip install pandas tk chardet
```

## How It Works

1. The tool reads the first column of two selected CSV files.
2. It compares the rows based on the first three characters (ID prefix).
3. If a variable from the first file is missing in the second file, the entire row is appended to the second file, with its ID prefix updated to match the second file’s format.
4. The updated file is saved to a user-specified location.

## How to Use

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/csv-file-comparator.git
```

2. **Run the Script**:

```bash
python file_comparator.py
```

3. **Use the GUI**:
   - Click the "Compare Files" button to select two CSV files.
   - The tool will process the files and identify missing rows.
   - A save dialog will appear, allowing you to save the updated file.

4. **Review the Output**:
   - The updated file will include all variables from the first file, with IDs modified to match the second file’s naming convention.

## Example Use Case

### Input Files:

**File 1:**

| Variable                |
|-------------------------|
| SLD_MV_RTR1_CB_OPEN      |
| SLD_MV_INC1_CB_CLOSE     |
| SLD_MV_RTR2_CB_CLOSE     |

**File 2:**

| Variable                |
|-------------------------|
| KUN_MV_RTR1_CB_OPEN      |
| KUN_MV_INC1_CB_CLOSE     |

### After Comparison:

The tool will append missing rows from **File 1** into **File 2**, adapting the `SLD_` prefix to `KUN_`.

**Updated File 2:**

| Variable                |
|-------------------------|
| KUN_MV_RTR1_CB_OPEN      |
| KUN_MV_INC1_CB_CLOSE     |
| KUN_MV_RTR2_CB_CLOSE     |

The updated file will also include the full details (rows) for the missing variables from File 1.

## Applications

- **Data Management**: Ensure consistency between CSV files, especially when working with datasets that follow naming conventions.
- **SCADA Systems**: Manage variable definitions and update missing entries, as in projects like Zenon.
- **General CSV Handling**: Compare and merge data from multiple CSV files in any domain.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit pull requests, or suggest new features.

---

This tool simplifies the process of comparing and updating data in CSV files, ensuring consistency and saving time.
```

### Updates:
- Generalized the tool description.
- Added a **How It Works** section to explain the steps clearly.
- Kept SCADA Zenon as a subtle example under **Applications**.
- Provided an illustrative example to demonstrate input and output. 

This version is suitable for broader audiences while retaining relevance to SCADA projects like Zenon.