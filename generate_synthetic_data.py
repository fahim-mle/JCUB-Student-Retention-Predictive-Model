#!/usr/bin/env python3
"""
Generate Synthetic Student Data
Production script to create full synthetic dataset based on research patterns
"""

from synthetic_data_generator import SyntheticStudentDataGenerator
import pandas as pd
import sys

def main():
    print("=" * 80)
    print("JCUB STUDENT RETENTION PREDICTIVE MODEL")
    print("Synthetic Data Generation")
    print("=" * 80)
    
    # Get number of students from command line or use default
    n_students = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    
    print(f"Generating {n_students} synthetic student records...")
    print("This dataset follows research-backed patterns for student retention prediction.\n")
    
    # Initialize generator
    generator = SyntheticStudentDataGenerator(n_students=n_students, random_state=42)
    
    # Generate full dataset
    df = generator.generate_full_dataset(n_students=n_students)
    
    # Create additional exports
    print("\n=== CREATING ADDITIONAL EXPORTS ===")
    
    # Export training/testing splits
    train_size = int(len(df) * 0.8)
    df_train = df.iloc[:train_size]
    df_test = df.iloc[train_size:]
    
    df_train.to_csv('synthetic_student_data_train.csv', index=False)
    df_test.to_csv('synthetic_student_data_test.csv', index=False)
    
    print(f"✓ Training set: {len(df_train)} records → synthetic_student_data_train.csv")
    print(f"✓ Test set: {len(df_test)} records → synthetic_student_data_test.csv")
    
    # Generate summary statistics
    print("\n=== DATASET SUMMARY ===")
    print(f"Total records: {len(df)}")
    print(f"Total features: {len(df.columns)}")
    print(f"Academic status distribution:")
    status_counts = df['academic_status'].value_counts()
    for status, count in status_counts.items():
        print(f"  {status}: {count} ({count/len(df)*100:.1f}%)")
    
    print(f"\\nAttendance vs Performance correlation: {df['attendance_1'].corr(df['subject_1_assess_1']):.3f}")
    print(f"Average first assessment score: {df['subject_1_assess_1'].mean():.1f}")
    print(f"Students with follow-up support: {(df['follow_up'] == 'Yes').sum()} ({(df['follow_up'] == 'Yes').mean()*100:.1f}%)")
    
    print("\n=== GENERATION COMPLETE ===")
    print("Files created:")
    print("  - synthetic_student_data.csv (main dataset)")
    print("  - synthetic_student_data_train.csv (training set)")
    print("  - synthetic_student_data_test.csv (test set)")
    print("\\nDataset ready for student retention prediction modeling!")

if __name__ == "__main__":
    main()