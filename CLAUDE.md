# JCUB Student Retention Predictive Model

## Project Overview
This project contains tools and models for predicting student retention at JCUB (Jamaica College University of Business).

## Project Structure
- `file_converter/` - Excel to CSV conversion utilities
- `documentation/` - Project documentation
- `instruction/` - Setup and usage instructions
- `student_data.xlsx` - Student data (converted to CSV in file_converter/output_csv/)

## Development Setup
1. Create virtual environment: `python3 -m venv venv`
2. Activate virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install pandas openpyxl`

## File Converter Usage
```bash
cd file_converter
source ../venv/bin/activate
python excel_to_csv.py <excel_file>
python excel_to_csv.py --all [directory]
```

## Git Commands
- Check status: `git status`
- Add files: `git add .`
- Commit: `git commit -m "message"`
- Push: `git push origin main`

## Testing
No specific test framework configured yet.

## Dependencies
- pandas
- openpyxl