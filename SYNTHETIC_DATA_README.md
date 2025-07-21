# JCUB Synthetic Student Data Documentation

## Overview

This synthetic dataset contains 2,000 student records generated for the JCUB Student Retention Predictive Model. The data represents **mid-semester snapshots** designed for early prediction of student risk factors. The dataset follows research-backed patterns for student success prediction and maintains realistic relationships between academic performance, attendance, and support interventions.

## Dataset Statistics

- **Total Records**: 2,000 students
- **Features**: 38 columns matching original dataset structure
- **Risk Distribution**: 60% low risk, 25% medium risk, 12% high risk, 3% critical risk
- **Temporal Context**: Mid-semester data (assessments 3 & 4 blank for prediction)
- **Submission Patterns**: 65% submit both assessments, 32% submit only assessment 1, 3% submit neither
- **Format**: CSV files with proper headers and data types

## Files Generated

1. **`synthetic_student_data.csv`** - Main dataset (2,000 records)
2. **`synthetic_student_data_train.csv`** - Training set (1,600 records, 80%)
3. **`synthetic_student_data_test.csv`** - Test set (400 records, 20%)

## Key Research-Backed Patterns

### Mid-Semester Assessment Strategy

- **Assessments 3 & 4** are intentionally blank/None to simulate mid-semester prediction scenarios
- **Assessment 1** is the strongest early predictor (78% accuracy for semester outcome)
- **Assessment 2** shows intervention effects and student progression patterns
- Only early-semester data available for risk prediction modeling

### Realistic Submission Patterns

- **65% of students** submit both assessment 1 and 2 (typical engaged students)
- **32% of students** submit only assessment 1 (struggling with progression)
- **3% of students** submit neither assessment (high-risk, from 'New'/'First year' cohorts or with failed subjects)
- Non-submitters are strategically assigned to realistic demographic groups

### Academic Performance

- **Assessment 1** is the strongest predictor (78% accuracy for semester outcome)
- **Subject 1** typically shows lowest scores (foundational filter effect)
- Students with interventions show 5-15% improvement in assessment 2
- Grade distribution varies by risk level: Low-risk (mean: 75), Medium-risk (mean: 60), High-risk (mean: 45), Critical-risk (mean: 30)


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

- **Attendance-Grade Correlation**: 0.502 (target: ~0.44 from research)
- **High-Risk Follow-up Rate**: 82.3% (realistic intervention rates)
- **Submission Pattern Validation**: 100% of non-submitters meet eligibility criteria
- **Missing Data Patterns**:
  - Failed subjects: 83.9% missing (most students don't fail)
  - Study skills: 77.8% missing (only struggling students attend)
  - Referral: 77.4% missing (majority don't need referrals)
  - Assessment 1: 3.0% missing (non-submitters)
  - Assessment 2: 35.0% missing (non-submitters + assessment-1-only group)

## Column Descriptions

### Core Demographics

- `student_id`: Unique identifier (10000-99999)
- `course`: Program of study (15 different programs)
- `student_cohort`: Entry status (New, Continuing, Return to Study, etc.)
- `academic_status`: Current standing (Satisfactory, At Risk, Excluded, etc.)

### Academic Performance

- `subject_1_assess_1`, `subject_1_assess_2`: Assessment scores (0-100, or None for non-submitters)
- `subject_1_assess_3`, `subject_1_assess_4`: Blank/None (mid-semester prediction scenario)
- `subject_2_assess_1`, `subject_2_assess_2`: Assessment scores (0-100, or None for non-submitters)
- `subject_2_assess_3`, `subject_2_assess_4`: Blank/None (mid-semester prediction scenario)
- `subject_3_assess_1`, `subject_3_assess_2`: Assessment scores (0-100, or None for non-submitters)
- `subject_3_assess_3`, `subject_3_assess_4`: Blank/None (mid-semester prediction scenario)
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
2. Focus on available early indicators (attendance_1, subject_1_assess_1, subject_1_assess_2) for prediction
3. Handle missing assessment data appropriately (32% have only assess_1, 3% have none)
4. Consider risk-based sampling for balanced training
5. Account for realistic submission patterns in feature engineering

### Model Validation

1. Use `synthetic_student_data_test.csv` for final evaluation
2. Test intervention effectiveness using follow-up data
3. Validate early warning system accuracy

### Feature Engineering

- Combine attendance patterns across subjects
- Create assessment progression trends from available assessments (1 & 2)
- Engineer submission pattern features (submitted both/assess1_only/none)
- Use support system data as intervention indicators
- Consider text analysis of comments for sentiment
- Handle missing assessment data with imputation or indicator variables

## Generated Using

- **Generator**: `synthetic_data_generator.py` (comprehensive class-based generator)
- **Production Script**: `generate_synthetic_data.py` (command-line interface)
- **Random Seed**: 42 (for reproducibility)
- **Research Base**: Academic literature on student retention patterns
- **Key Features**: 
  - Risk-based student profiling
  - Realistic submission pattern simulation
  - Mid-semester temporal context
  - Course-subject mapping integration
  - Research-validated correlation patterns

## Next Steps

1. Load datasets into your preferred ML framework
2. Explore correlation patterns between early indicators and outcomes
3. Build predictive models using mid-semester data (assessments 1-2, attendance patterns)
4. Handle missing assessment data strategically in your modeling pipeline
5. Test intervention effectiveness using support system variables
6. Validate model performance against research benchmarks
7. Experiment with submission pattern features as risk indicators

## Important Notes for Analysis

- **Missing Data is Intentional**: Assessment 3 & 4 missing values represent mid-semester scenario, not data quality issues
- **Submission Patterns**: Non-submission is a strong risk indicator - treat missing assessment data as meaningful
- **Temporal Context**: Model should predict using only early-semester information available at mid-semester
- **Demographic Targeting**: Non-submitters are realistically assigned to 'New'/'First year' cohorts and students with prior failures

This synthetic dataset provides a realistic foundation for developing and testing **mid-semester** student retention prediction models while maintaining data privacy and following established research patterns.