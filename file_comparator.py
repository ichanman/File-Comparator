from tkinter import Tk, filedialog, Button, Label
import pandas as pd

def get_file_encoding(file_path):
    """
    Detect the encoding of a file using chardet or similar method.
    This function should be customized to suit your file encoding detection.
    """
    import chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def append_missing_variables(file1_path, file2_path):
    """
    Appends missing variables from file1 to file2 with modified IDs and saves to a new file.
    """
    # Read the first columns of both files
    df1 = pd.read_csv(file1_path, encoding=get_file_encoding(file1_path))  # Entire file for row extraction
    df2 = pd.read_csv(file2_path, encoding=get_file_encoding(file2_path))  # Entire file for appending

    # Extract IDs and variables
    col1 = df1.iloc[:, 0].str.strip()  # First column of file1
    col2 = df2.iloc[:, 0].str.strip()  # First column of file2
    vars1 = col1.str[4:]  # Variable names after the 3-character ID
    vars2 = col2.str[4:]

    # Identify the ID prefix for each file
    id1 = col1.str[:3].iloc[0]  # Extract ID from first row of file1
    id2 = col2.str[:3].iloc[0]  # Extract ID from first row of file2

    # Identify missing variables
    missing_vars = vars1[~vars1.isin(vars2)].index  # Indices of missing variables in file1

    # Extract and modify rows for missing variables
    missing_rows = df1.iloc[missing_vars].copy()  # Extract entire rows of missing variables
    missing_rows.iloc[:, 0] = missing_rows.iloc[:, 0].str.replace(id1, id2, n=1)  # Replace ID prefix

    # Append missing rows to file2 content
    updated_df2 = pd.concat([df2, missing_rows], ignore_index=True)

    # Open save dialog to let the user select the output file path
    output_file_path = filedialog.asksaveasfilename(
        title="Save Updated File", 
        defaultextension=".csv", 
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    
    # If user selects a file, save the updated dataframe
    if output_file_path:
        updated_df2.to_csv(output_file_path, index=False, encoding=get_file_encoding(file2_path))
        print(f"Updated file saved to {output_file_path}")
    else:
        print("No file selected. Save operation cancelled.")

def create_gui():
    """
    GUI to select files and compare the first columns.
    """
    root = Tk()
    root.title("File Comparator")
    root.geometry("400x200")

    def on_compare():
        # File selection dialogs
        file1_path = filedialog.askopenfilename(title="Select First File", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        file2_path = filedialog.askopenfilename(title="Select Second File", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        
        if file1_path and file2_path:
            append_missing_variables(file1_path, file2_path)

    Label(root, text="File Comparator Tool", font=("Arial", 14)).pack(pady=10)
    Button(root, text="Compare Files", command=on_compare).pack(pady=20)
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
