#!/usr/bin/env python3
"""
Student Data Analysis Script
Analyzes original dataset to extract patterns for synthetic data generation
"""

import pandas as pd
import numpy as np
from collections import Counter

def analyze_original_data():
    """Analyze the original student dataset to understand patterns"""
    
    # Load the original dataset
    df = pd.read_csv('file_converter/output_csv/student_data.csv')
    
    print("=== ORIGINAL DATASET ANALYSIS ===")
    print(f"Dataset shape: {df.shape}")
    print(f"Total students: {len(df)}")
    
    # Basic info
    print("\n=== COLUMN INFORMATION ===")
    print(df.info())
    
    print("\n=== CATEGORICAL VALUES ANALYSIS ===")
    
    categorical_columns = [
        'course', 'student_cohort', 'academic_status', 'failed_subjects',
        'study_skills(attended)', 'referral', 'pp_meeting', 'self_assessment',
        'readiness_assessment_results', 'follow_up', 'follow_up_type',
        'learn_jcu_issues_1', 'lecturer_referral_1',
        'learn_jcu_issues_2', 'lecturer_referral_2', 
        'learn_jcu_issues_3', 'lecturer_referral_3'
    ]
    
    for col in categorical_columns:
        if col in df.columns:
            print(f"\n{col}:")
            value_counts = df[col].value_counts(dropna=False)
            print(value_counts)
            print(f"  Unique values: {df[col].nunique()}")
            print(f"  Missing values: {df[col].isnull().sum()}")
    
    print("\n=== NUMERICAL STATISTICS ===")
    
    numerical_columns = [
        'subject_1_assess_1', 'subject_1_assess_2', 'subject_1_assess_3', 'subject_1_assess_4',
        'attendance_1', 'subject_2_assess_1', 'subject_2_assess_2', 'subject_2_assess_3', 
        'subject_2_assess_4', 'attendance_2', 'subject_3_assess_1', 'subject_3_assess_2', 
        'subject_3_assess_3', 'attendance_3'
    ]
    
    for col in numerical_columns:
        if col in df.columns:
            print(f"\n{col}:")
            print(f"  Mean: {df[col].mean():.2f}")
            print(f"  Std: {df[col].std():.2f}")
            print(f"  Min: {df[col].min():.2f}")
            print(f"  Max: {df[col].max():.2f}")
            print(f"  Missing: {df[col].isnull().sum()}")
    
    print("\n=== RISK DISTRIBUTION ANALYSIS ===")
    
    # Analyze academic status distribution
    if 'academic_status' in df.columns:
        status_counts = df['academic_status'].value_counts()
        total = len(df)
        print("Academic Status Distribution:")
        for status, count in status_counts.items():
            percentage = (count / total) * 100
            print(f"  {status}: {count} ({percentage:.1f}%)")
    
    # Analyze attendance patterns
    print("\n=== ATTENDANCE PATTERNS ===")
    if 'attendance_1' in df.columns:
        attendance_ranges = pd.cut(df['attendance_1'], bins=[0, 50, 70, 85, 100], 
                                 labels=['<50%', '50-70%', '70-85%', '85-100%'])
        print("Attendance_1 Distribution:")
        print(attendance_ranges.value_counts())
    
    return df

if __name__ == "__main__":
    df = analyze_original_data()