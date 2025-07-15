# Synthetic Student Data Generation Process

## Step 1: Setup and Preparation

### 1.1 Install Required Packages

```bash
pip install pandas numpy faker scipy scikit-learn
```

### 1.2 Load Original Dataset

- Import the original `student_data.csv`
- Analyze existing categorical values for each column
- Extract unique values from categorical columns to maintain consistency
- Document the data structure and patterns

### 1.3 Create Risk Distribution Framework

- Define 4 risk levels: low_risk (60%), medium_risk (25%), high_risk (12%), critical_risk (3%)
- This matches the client's real-world pattern of 300/2000 students needing support

## Step 2: Generate Core Student Profiles

### 2.1 Basic Profile Generation

- **student_id**: Generate unique random integers (10000-99999)
- **course**: Use original categorical values with realistic distribution
- **student_cohort**: Use existing format (YYYY_SX) with appropriate weights
- **academic_status**: Map to risk levels (low→good_standing, high→at_risk, etc.)

### 2.2 Academic Performance Generation

- **failed_subjects**: Generate based on risk level (low=mostly 0, high=1-3+)
- **subject_1, subject_2, subject_3**: Generate grades using normal distribution per risk level
- **Assessment scores**: Create progressive patterns (assess_1 most predictive)

## Step 3: Generate Attendance Patterns

### 3.1 Attendance Logic

- **attendance_1**: Most critical (first 3 weeks rule)
- **attendance_2, attendance_3**: Show decline patterns for high-risk students
- **Correlation**: Higher attendance = better grades (research-backed)

### 3.2 Attendance Distribution

- Low risk: 85-95% average
- Medium risk: 70-85% average  
- High risk: 50-70% average
- Critical risk: <50% average

## Step 4: Generate Support System Data

### 4.1 Referral System

- **referral**: Based on risk probability (low=5%, critical=90%)
- **lecturer_referral_1/2/3**: Subject-specific referrals
- **pp_meeting**: Only for high-risk students (reserved intervention)

### 4.2 Follow-up Actions

- **follow_up**: Institutional response rates by risk level
- **follow_up_type**: Use original categories with appropriate weights
- **study_skills(attended)**: Struggling students more likely to attend

## Step 5: Generate Behavioral Indicators

### 5.1 Platform Issues

- **learn_jcu_issues_1/2/3**: Use original issue categories
- Generate realistic patterns (digital literacy, English language, etc.)
- Higher risk students have more issues across multiple subjects

### 5.2 Student Assessment Data

- **self_assessment**: Use original categories (financial stress, family issues, etc.)
- **readiness_assessment_results**: Institutional risk classification
- Map to risk levels with realistic accuracy (85% correlation)

## Step 6: Generate Text Fields

### 6.1 Comments and Issues

- **comments**: Generate realistic staff observations
- **identified_issues**: Create intervention notes
- More detailed entries for high-risk students

### 6.2 Missing Data Patterns

- High performers: Sparse support data (no intervention needed)
- Critical risk: Complete monitoring data
- Random missing: 2-5% across all columns

## Step 7: Data Validation and Quality Control

### 7.1 Consistency Checks

- Ensure attendance correlates with grades
- Verify support system logic (multiple referrals → pp_meeting)
- Check temporal patterns (early indicators predict later outcomes)

### 7.2 Realistic Constraints

- Assessment scores should progress logically
- Support interventions should show timing effects
- Missing data should follow realistic patterns

## Step 8: Scale and Export

### 8.1 Data Generation

- Generate 2000-5000 synthetic records
- Maintain original dataset structure (38 columns)
- Combine with original 698 records if needed

### 8.2 Export Options

- Save as CSV matching original format
- Create separate train/test splits
- Document generation parameters and assumptions

## Step 9: Validation Against Research

### 9.1 Statistical Validation

- Verify attendance-grade correlation matches research (0.44)
- Check early warning effectiveness (assess_1 predicts 78% of outcomes)
- Validate support intervention success rates (65-75%)

### 9.2 Real-world Alignment

- Confirm risk distribution matches client data (15% need intervention)
- Validate missing data patterns are realistic
- Check categorical distributions match university patterns

## Implementation Notes

- Use the original categorical values exactly as they appear in the dataset
- Implement risk-based generation for realistic patterns
- Include research-backed biases (STEM higher failure rates, attendance critical, etc.)
- Generate progressive assessment patterns showing intervention effects
- Create realistic missing data patterns (not random missing)

This process will create a synthetic dataset that maintains the original structure while incorporating real-world student success patterns from the research literature.
