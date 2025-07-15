# JCUB Synthetic Student Data Documentation

## Overview

This synthetic dataset contains 2,000 student records generated for the JCUB Student Retention Predictive Model. The data follows research-backed patterns for student success prediction and maintains realistic relationships between academic performance, attendance, and support interventions.

## Dataset Statistics

- **Total Records**: 2,000 students
- **Features**: 38 columns matching original dataset structure
- **Risk Distribution**: 60% low risk, 25% medium risk, 12% high risk, 3% critical risk
- **Format**: CSV files with proper headers and data types

## Files Generated

1. **`synthetic_student_data.csv`** - Main dataset (2,000 records)
2. **`synthetic_student_data_train.csv`** - Training set (1,600 records, 80%)
3. **`synthetic_student_data_test.csv`** - Test set (400 records, 20%)

## Key Research-Backed Patterns

### Academic Performance

- **Assessment 1** is the strongest predictor (78% accuracy for semester outcome)
- **Subject 1** typically shows lowest scores (foundational filter effect)
- Students with interventions show 5-15% improvement over semester
- Grade distribution: 25% high (>75), 50% average (50-75), 25% struggling (<50)

### Attendance Patterns

- **First 3 weeks** are critical for prediction
- >95% attendance correlates with A/B grades
- Each 10% attendance drop ≈ 6-8 grade point decrease
- High-risk students show 15-30% decline pattern

### Support System Logic

- 15% of students need intervention (matching 300/2000 client data)
- PP meetings reserved for 8% highest risk students
- Follow-up effectiveness decreases if delayed >2 weeks
- Support paradox: More support data = initially struggling students

### Risk Level Distribution

- **Low Risk (60%)**: Good attendance (>85%), grades (>65%), minimal support needs
- **Medium Risk (25%)**: Moderate attendance (70-85%), grades (50-65%), some support utilization
- **High Risk (12%)**: Poor attendance (<70%), grades (<50%), multiple interventions
- **Critical Risk (3%)**: Multiple failures, unresponsive, major barriers

## Data Quality Metrics

- **Attendance-Grade Correlation**: 0.525 (target: ~0.44 from research)
- **High-Risk Follow-up Rate**: 82.3% (realistic intervention rates)
- **Missing Data Patterns**:
  - Failed subjects: 83.9% missing (most students don't fail)
  - Study skills: 77.8% missing (only struggling students attend)
  - Referral: 77.4% missing (majority don't need referrals)

## Column Descriptions

### Core Demographics

- `student_id`: Unique identifier (10000-99999)
- `course`: Program of study (15 different programs)
- `student_cohort`: Entry status (New, Continuing, Return to Study, etc.)
- `academic_status`: Current standing (Satisfactory, At Risk, Excluded, etc.)

### Academic Performance

- `subject_1_assess_1` to `subject_1_assess_4`: Assessment scores (0-100)
- `subject_2_assess_1` to `subject_2_assess_4`: Assessment scores (0-100)
- `subject_3_assess_1` to `subject_3_assess_3`: Assessment scores (0-100)
- `subject_4_assess_4`: Final assessment for subject 3 (original format)
- `attendance_1`, `attendance_2`, `attendance_3`: Attendance percentages

### Support System

- `failed_subjects`: Previously failed subject codes
- `study_skills(attended)`: Type of academic support attended
- `referral`: Referral source for support
- `pp_meeting`: Personal Progress meeting status
- `self_assessment`: Student self-reported issues (Yes/No)
- `follow_up`: Whether follow-up occurred (Yes/No)
- `follow_up_type`: Type of follow-up (Email, Phone, F2F, No Reply)

### Behavioral Indicators

- `learn_jcu_issues_1/2/3`: Learning platform access issues
- `lecturer_referral_1/2/3`: Lecturer concern categories
- `readiness_assessment_results`: Institutional risk assessment
- `comments`: Staff observations and interventions
- `identified_issues`: Categorized student challenges

## Usage Recommendations

### Model Training

1. Use `synthetic_student_data_train.csv` for model development
2. Focus on early indicators (attendance_1, subject_1_assess_1) for prediction
3. Consider risk-based sampling for balanced training

### Model Validation

1. Use `synthetic_student_data_test.csv` for final evaluation
2. Test intervention effectiveness using follow-up data
3. Validate early warning system accuracy

### Feature Engineering

- Combine attendance patterns across subjects
- Create assessment progression trends
- Use support system data as intervention indicators
- Consider text analysis of comments for sentiment

## Generated Using

- **Generator**: `synthetic_data_generator.py`
- **Production Script**: `generate_synthetic_data.py`
- **Random Seed**: 42 (for reproducibility)
- **Research Base**: Academic literature on student retention patterns

## Next Steps

1. Load datasets into your preferred ML framework
2. Explore correlation patterns between early indicators and outcomes
3. Build predictive models using first 3 weeks of data
4. Test intervention effectiveness using support system variables
5. Validate model performance against research benchmarks

This synthetic dataset provides a realistic foundation for developing and testing student retention prediction models while maintaining data privacy and following established research patterns.