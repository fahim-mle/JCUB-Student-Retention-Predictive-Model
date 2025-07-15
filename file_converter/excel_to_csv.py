import pandas as pd
import os
import sys
from pathlib import Path

def convert_excel_to_csv(input_file, output_dir="output_csv"):
    try:
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        os.makedirs(output_dir, exist_ok=True)
        
        file_name = Path(input_file).stem
        
        if input_file.endswith(('.xlsx', '.xls')):
            excel_file = pd.ExcelFile(input_file)
            
            if len(excel_file.sheet_names) == 1:
                df = pd.read_excel(input_file)
                output_file = os.path.join(output_dir, f"{file_name}.csv")
                df.to_csv(output_file, index=False)
                print(f"Converted: {input_file} -> {output_file}")
            else:
                for sheet_name in excel_file.sheet_names:
                    df = pd.read_excel(input_file, sheet_name=sheet_name)
                    output_file = os.path.join(output_dir, f"{file_name}_{sheet_name}.csv")
                    df.to_csv(output_file, index=False)
                    print(f"Converted sheet '{sheet_name}': {input_file} -> {output_file}")
        else:
            print(f"Error: '{input_file}' is not a valid Excel file.")
            return False
        
        return True
    
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")
        return False

def convert_all_excel_files(input_dir=".", output_dir="output_csv"):
    excel_files = []
    for ext in ['*.xlsx', '*.xls']:
        excel_files.extend(Path(input_dir).glob(ext))
    
    if not excel_files:
        print(f"No Excel files found in '{input_dir}'")
        return
    
    success_count = 0
    for excel_file in excel_files:
        if convert_excel_to_csv(str(excel_file), output_dir):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(excel_files)} files converted successfully.")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python excel_to_csv.py <excel_file>")
        print("  python excel_to_csv.py --all [input_directory]")
        print("\nExamples:")
        print("  python excel_to_csv.py data.xlsx")
        print("  python excel_to_csv.py --all")
        print("  python excel_to_csv.py --all /path/to/excel/files")
        return
    
    if sys.argv[1] == "--all":
        input_dir = sys.argv[2] if len(sys.argv) > 2 else "."
        convert_all_excel_files(input_dir)
    else:
        input_file = sys.argv[1]
        convert_excel_to_csv(input_file)

if __name__ == "__main__":
    main()