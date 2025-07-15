# Step-by-Step Data Processing Pipeline

## Step 1: Data Exploration & Audit

### OBJECTIVE: Understand current data quality and patterns

*ACTIONS:*
1.1 Load dataset and examine basic structure
    - Check data types, shape, column names
    - Identify numerical vs categorical columns
    - Document any naming inconsistencies

1.2 Missing value analysis
    - Calculate missing percentage per column
    - Identify patterns in missingness (random vs systematic)
    - Flag columns with >70% missing (consider dropping)

1.3 Data distribution analysis
    - Plot histograms for numerical columns
    - Check value ranges (grades 0-100, attendance 0-100)
    - Identify outliers and anomalies

1.4 Target variable analysis
    - Examine 'academic_status' unique values
    - Check class distribution/imbalance
    - Cross-tabulate with other key variables

OUTPUTS: data_audit_report.html, missing_value_heatmap.png

## Step 2: Data Cleaning & Standardization

### OBJECTIVE: Create clean, consistent dataset

*ACTIONS:*
2.1 Handle missing values
    - Numerical: Use median for grades/attendance
    - Categorical: Create 'Unknown' category or mode imputation
    - Strategic: Some missing values are informative (no follow_up = good)

2.2 Standardize categorical values
    - Clean inconsistent entries ('yes'/'Yes'/'YES' → 'Yes')
    - Handle null representations ('NaN', 'NULL', '', 'N/A')
    - Create consistent value mappings

2.3 Grade standardization
    - Convert all grades to 0-100 percentage scale
    - Handle different formats (fraction, letter grades, percentages)
    - Validate grade ranges (0-100)

2.4 Attendance standardization
    - Ensure all attendance values are 0-100 percentages
    - Handle impossible values (>100%, negative)
    - Create missing attendance flags

2.5 Remove duplicates and invalid records
    - Check for duplicate student_ids
    - Flag records with impossible data combinations
    - Handle partial duplicates

OUTPUTS: cleaned_dataset.csv, cleaning_log.txt

## Step 3: Feature Engineering - Academic Performance

### OBJECTIVE: Create meaningful academic indicators

*ACTIONS:*
3.1 Grade aggregation features
    - avg_subject_grade: Mean of subject_1, subject_2, subject_3
    - failing_subjects_count: Count of subjects with grade < 50
    - grade_variance: Variance across subjects (consistency indicator)
    - lowest_subject_grade: Minimum grade across subjects

3.2 Assessment progression features
    - For each subject, calculate:

      * assessment_trend: Linear slope of assess_1 to assess_4
      * assessment_volatility: Standard deviation of assessments
      * early_performance: Average of assess_1 and assess_2
      * late_performance: Average of assess_3 and assess_4
      * improvement_rate: (late_performance - early_performance)

3.3 Critical early warning indicators
    - first_assessment_risk: Boolean if any assess_1 < 45
    - early_failure_pattern: Count of assess_1 scores < 50
    - assessment_1_avg: Average of all subject assess_1 scores

3.4 Grade quality indicators
    - consistent_performer: Boolean if grade_variance < threshold
    - subject_specialty: Identify strongest/weakest subject
    - grade_trajectory: Overall improving/declining/stable

OUTPUTS: academic_features.csv

## Step 4: Feature Engineering - Behavioral Indicators

### OBJECTIVE: Create behavioral risk indicators based on client insights

*ACTIONS:*
4.1 Attendance patterns
    - avg_attendance: Mean attendance across all subjects
    - attendance_decline: attendance_1 - attendance_3
    - early_attendance_risk: Boolean if attendance_1 < 70
    - attendance_consistency: Standard deviation of attendance
    - critical_attendance: Boolean if any attendance < 50

4.2 Engagement indicators
    - platform_issues_count: Count of non-null learn_jcu_issues
    - engagement_risk: Boolean if multiple learn_jcu_issues
    - digital_literacy_flag: Boolean if issues contain 'digital'/'laptop'
    - language_support_flag: Boolean if issues contain 'English'/'translate'

4.3 Communication patterns
    - lecturer_referral_count: Count of 'Yes' across all lecturer_referrals
    - escalation_pattern: Boolean if referrals increase over time
    - communication_breakdown: Boolean if 'unresponsive' mentioned
    - proactive_communication: Boolean if student initiated contact

4.4 Timeline indicators
    - early_warning_week: First week where issues appeared
    - issue_persistence: Boolean if same issues across multiple subjects
    - intervention_timeline: Gap between issue identification and support

OUTPUTS: behavioral_features.csv

## Step 5: Feature Engineering - Support System Interaction

### OBJECTIVE: Capture support system utilization and effectiveness

*ACTIONS:*
5.1 Support utilization features
    - total_support_touchpoints: Count of all support interactions
    - support_types_used: Count of different support types accessed
    - study_skills_attended: Boolean conversion
    - pp_meeting_held: Boolean conversion
    - follow_up_received: Boolean conversion

5.2 Support effectiveness indicators
    - support_response_time: Time between issue and intervention
    - intervention_success: Grade improvement after support
    - support_engagement: Student responsiveness to support
    - multi_support_user: Boolean if used multiple support types

5.3 Risk escalation features
    - referral_to_support_ratio: Referrals vs actual support received
    - support_adequacy: Whether support matched identified issues
    - intervention_timing: Early vs late intervention flag
    - support_completion: Whether student completed recommended support

5.4 Outcome correlation features
    - pre_support_performance: Academic metrics before intervention
    - post_support_performance: Academic metrics after intervention
    - support_impact_score: Quantified improvement attribution

OUTPUTS: support_features.csv

## Step 6: Feature Engineering - Risk Profiling

### OBJECTIVE: Create comprehensive risk indicators matching client insights

*ACTIONS:*
6.1 Multi-dimensional risk scoring
    - academic_risk_score: Weighted combination of grade/assessment factors
    - behavioral_risk_score: Attendance + engagement factors
    - support_need_score: Based on identified issues and interventions
    - early_warning_score: First 3 weeks indicators

6.2 Risk category classification
    - financial_stress_indicators: PT job mentions, transport issues
    - mental_health_indicators: Stress/anxiety mentions in assessments
    - academic_readiness_indicators: Language, digital literacy issues
    - social_integration_indicators: Engagement, participation patterns

6.3 Temporal risk features
    - risk_trajectory: Improving/stable/declining over time
    - critical_period_risk: Specific high-risk timeframes
    - intervention_responsiveness: How quickly risk factors respond to support
    - risk_persistence: Whether risk factors are temporary or ongoing

6.4 Composite risk indicators
    - overall_risk_level: Combined score across all dimensions
    - primary_risk_factor: Dominant risk category
    - intervention_priority: Urgency ranking
    - success_probability: Likelihood of improvement with intervention

OUTPUTS: risk_profile_features.csv

## Step 7: Feature Validation & Selection

### OBJECTIVE: Validate feature quality and select optimal feature set

*ACTIONS:*
7.1 Feature quality assessment
    - Check for multicollinearity (correlation matrix)
    - Identify redundant features (high correlation)
    - Validate feature distributions (no constant values)
    - Check for data leakage (future information)

7.2 Feature importance analysis
    - Use Random Forest for feature importance ranking
    - Calculate mutual information with target variable
    - Identify most predictive features for each risk category
    - Document feature interpretation and business meaning

7.3 Feature selection strategies
    - Remove highly correlated features (>0.9 correlation)
    - Select top N features by importance
    - Ensure representation across all risk dimensions
    - Balance interpretability vs predictive power

7.4 Final feature set documentation
    - Create feature dictionary with definitions
    - Document data sources and calculation methods
    - Note any assumptions or limitations
    - Prepare feature set for modeling

OUTPUTS: final_feature_set.csv, feature_importance_report.html, feature_dictionary.json

## Step 8: Data Preparation for Modeling

### OBJECTIVE: Prepare clean, engineered dataset for machine learning

*ACTIONS:*
8.1 Final data integration
    - Merge all feature sets on student_id
    - Handle any remaining missing values
    - Validate data consistency across feature sets
    - Create final modeling dataset

8.2 Data preprocessing
    - Scale numerical features (StandardScaler)
    - Encode categorical features (LabelEncoder/OneHot)
    - Handle class imbalance if present
    - Create train/validation/test splits

8.3 Quality assurance
    - Final data validation checks
    - Ensure no data leakage
    - Validate feature engineering logic
    - Create data lineage documentation

8.4 Export for modeling
    - Save processed dataset in multiple formats
    - Create data dictionary for modeling team
    - Document preprocessing steps
    - Prepare synthetic data generation rules

OUTPUTS: modeling_dataset.csv, preprocessing_pipeline.pkl, data_lineage.md
