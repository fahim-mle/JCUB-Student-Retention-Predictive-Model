#!/usr/bin/env python3
"""
Synthetic Student Data Generator
Generates realistic student retention data based on research patterns
"""

import pandas as pd
import numpy as np
import random
from faker import Faker
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class SyntheticStudentDataGenerator:
    def __init__(self, n_students=2000, random_state=42):
        self.n_students = n_students
        self.random_state = random_state
        self.faker = Faker()
        
        # Set random seeds for reproducibility
        np.random.seed(random_state)
        random.seed(random_state)
        Faker.seed(random_state)
        
        # Load original data patterns
        self.original_df = pd.read_csv('file_converter/output_csv/student_data.csv')
        self.extract_original_patterns()
        
        # Risk distribution based on client data (300/2000 students needing support)
        self.risk_distribution = {
            'low_risk': 0.60,      # 60% - Good performance, minimal support
            'medium_risk': 0.25,   # 25% - Moderate performance, some support
            'high_risk': 0.12,     # 12% - Poor performance, multiple interventions
            'critical_risk': 0.03  # 3% - Multiple failures, unresponsive
        }
        
    def extract_original_patterns(self):
        """Extract patterns from original dataset"""
        
        # Categorical value mappings
        self.categorical_values = {
            'course': self.original_df['course'].unique().tolist(),
            'student_cohort': self.original_df['student_cohort'].unique().tolist(),
            'academic_status': self.original_df['academic_status'].unique().tolist(),
            'failed_subjects': [None] + [x for x in self.original_df['failed_subjects'].unique() if pd.notna(x)],
            'study_skills(attended)': self.original_df['study_skills(attended)'].unique().tolist(),
            'referral': self.original_df['referral'].unique().tolist(),
            'pp_meeting': self.original_df['pp_meeting'].unique().tolist(),
            'self_assessment': self.original_df['self_assessment'].unique().tolist(),
            'readiness_assessment_results': self.original_df['readiness_assessment_results'].unique().tolist(),
            'follow_up': self.original_df['follow_up'].unique().tolist(),
            'follow_up_type': self.original_df['follow_up_type'].unique().tolist(),
            'learn_jcu_issues': ['Access', 'No Access'],
            'lecturer_referral': ['Attendance', 'Non Submission', 'Concern for Welfare']
        }
        
        print("✓ Extracted categorical patterns from original dataset")
        
    def assign_risk_levels(self):
        """Assign risk levels to students based on distribution"""
        
        risk_levels = []
        
        # Calculate number of students per risk level
        n_low = int(self.n_students * self.risk_distribution['low_risk'])
        n_medium = int(self.n_students * self.risk_distribution['medium_risk'])
        n_high = int(self.n_students * self.risk_distribution['high_risk'])
        n_critical = self.n_students - n_low - n_medium - n_high  # Remainder
        
        # Assign risk levels
        risk_levels.extend(['low_risk'] * n_low)
        risk_levels.extend(['medium_risk'] * n_medium)
        risk_levels.extend(['high_risk'] * n_high)
        risk_levels.extend(['critical_risk'] * n_critical)
        
        # Shuffle to randomize order
        random.shuffle(risk_levels)
        
        print(f"✓ Risk level distribution: Low={n_low}, Medium={n_medium}, High={n_high}, Critical={n_critical}")
        
        return risk_levels
        
    def generate_basic_profiles(self, risk_levels):
        """Generate basic student profiles"""
        
        profiles = []
        
        for i, risk_level in enumerate(risk_levels):
            profile = {
                'student_id': random.randint(10000, 99999),
                'risk_level': risk_level
            }
            
            # Course selection (with some bias for risk levels)
            if risk_level == 'critical_risk':
                # Critical risk students more likely in challenging programs
                profile['course'] = np.random.choice([
                    'Master of Business Administration',
                    'Master of Information Technology',
                    'Master of Engineering Management'
                ], p=[0.4, 0.3, 0.3])
            else:
                # Other students more evenly distributed
                profile['course'] = np.random.choice(self.categorical_values['course'])
            
            # Student cohort with realistic weights
            cohort_weights = {
                'New': 0.20,
                'First year': 0.18,
                'Continuing': 0.15,
                'Return to Study': 0.12,
                'Transferred': 0.10,
                'SRI to JCUB': 0.10,
                'LOA': 0.08,
                'Excluded': 0.07
            }
            
            profile['student_cohort'] = np.random.choice(
                list(cohort_weights.keys()),
                p=list(cohort_weights.values())
            )
            
            # Academic status mapping to risk levels
            academic_status_mapping = {
                'low_risk': np.random.choice(['Satisfactory', 'Conditional'], p=[0.7, 0.3]),
                'medium_risk': np.random.choice(['Conditional', 'Academic Caution'], p=[0.6, 0.4]),
                'high_risk': np.random.choice(['Academic Caution', 'At Risk'], p=[0.4, 0.6]),
                'critical_risk': np.random.choice(['At Risk', 'Excluded'], p=[0.3, 0.7])
            }
            
            profile['academic_status'] = academic_status_mapping[risk_level]
            
            # Failed subjects based on risk level
            failed_subjects_prob = {
                'low_risk': 0.05,      # 5% have failed subjects
                'medium_risk': 0.20,   # 20% have failed subjects
                'high_risk': 0.50,     # 50% have failed subjects
                'critical_risk': 0.80  # 80% have failed subjects
            }
            
            if np.random.random() < failed_subjects_prob[risk_level]:
                profile['failed_subjects'] = np.random.choice([
                    'CP5639', 'CP5633', 'CP1401', 'CP1404', 'CP1407', 'CP1406', 'CP5046', 'CP5047'
                ])
            else:
                profile['failed_subjects'] = None
                
            profiles.append(profile)
            
        print(f"✓ Generated {len(profiles)} basic student profiles")
        return profiles
        
    def generate_support_system_data(self, profiles):
        """Generate support system related data"""
        
        for profile in profiles:
            risk_level = profile['risk_level']
            
            # Study skills attendance (struggling students more likely to attend)
            study_skills_prob = {
                'low_risk': 0.10,      # 10% attend
                'medium_risk': 0.30,   # 30% attend
                'high_risk': 0.60,     # 60% attend
                'critical_risk': 0.80  # 80% attend
            }
            
            if np.random.random() < study_skills_prob[risk_level]:
                profile['study_skills(attended)'] = np.random.choice(self.categorical_values['study_skills(attended)'])
            else:
                profile['study_skills(attended)'] = None
                
            # Referral system based on risk probability
            referral_prob = {
                'low_risk': 0.05,      # 5% get referrals
                'medium_risk': 0.30,   # 30% get referrals
                'high_risk': 0.70,     # 70% get referrals
                'critical_risk': 0.90  # 90% get referrals
            }
            
            if np.random.random() < referral_prob[risk_level]:
                profile['referral'] = np.random.choice(self.categorical_values['referral'])
            else:
                profile['referral'] = None
                
            # PP meeting (reserved for highest risk - 8% of all students)
            pp_meeting_prob = {
                'low_risk': 0.01,      # 1% get PP meetings
                'medium_risk': 0.05,   # 5% get PP meetings
                'high_risk': 0.25,     # 25% get PP meetings
                'critical_risk': 0.80  # 80% get PP meetings
            }
            
            if np.random.random() < pp_meeting_prob[risk_level]:
                profile['pp_meeting'] = np.random.choice(self.categorical_values['pp_meeting'])
            else:
                profile['pp_meeting'] = 'Not relevant'
                
            # Self assessment (students identify their own issues)
            self_assessment_prob = {
                'low_risk': 0.30,      # 30% do self assessment
                'medium_risk': 0.50,   # 50% do self assessment
                'high_risk': 0.70,     # 70% do self assessment
                'critical_risk': 0.60  # 60% do self assessment (some too disengaged)
            }
            
            profile['self_assessment'] = 'Yes' if np.random.random() < self_assessment_prob[risk_level] else 'No'
            
            # Readiness assessment results (institutional risk classification)
            # Using original single value for consistency
            profile['readiness_assessment_results'] = 'L/G:9/10 N:5/10 R:8/10'
            
            # Follow up (institutional response rates)
            follow_up_prob = {
                'low_risk': 0.20,      # 20% get follow up
                'medium_risk': 0.50,   # 50% get follow up
                'high_risk': 0.80,     # 80% get follow up
                'critical_risk': 0.90  # 90% get follow up
            }
            
            profile['follow_up'] = 'Yes' if np.random.random() < follow_up_prob[risk_level] else 'No'
            
            # Follow up type (if follow up exists)
            if profile['follow_up'] == 'Yes':
                profile['follow_up_type'] = np.random.choice(self.categorical_values['follow_up_type'])
            else:
                profile['follow_up_type'] = 'No Reply'
        
        print("✓ Generated support system data")
        return profiles
        
    def generate_academic_performance(self, profiles):
        """Generate academic performance data with realistic patterns"""
        
        for profile in profiles:
            risk_level = profile['risk_level']
            
            # Define grade distributions by risk level (research-backed)
            grade_params = {
                'low_risk': {'mean': 75, 'std': 12},      # Good performance
                'medium_risk': {'mean': 60, 'std': 15},   # Average performance
                'high_risk': {'mean': 45, 'std': 18},     # Poor performance
                'critical_risk': {'mean': 30, 'std': 20}  # Very poor performance
            }
            
            params = grade_params[risk_level]
            
            # Generate assessment scores for each subject
            for subject_num in range(1, 4):  # subjects 1, 2, 3
                
                # Assessment 1 is the strongest predictor (78% accuracy)
                # Generate base score with higher variance for prediction accuracy
                if subject_num == 1:
                    # Subject 1 typically lowest (foundational filter)
                    base_mean = params['mean'] - 5
                else:
                    base_mean = params['mean']
                    
                assess_1 = np.random.normal(base_mean, params['std'])
                assess_1 = np.clip(assess_1, 0, 100)
                
                # Subsequent assessments show patterns based on intervention
                intervention_effect = 0
                if profile['follow_up'] == 'Yes' and profile['pp_meeting'] != 'Not relevant':
                    # Students with intervention show 5-15% improvement
                    intervention_effect = np.random.uniform(5, 15)
                
                # Assessment 2: Slight improvement if intervention
                assess_2 = assess_1 + intervention_effect/2 + np.random.normal(0, 8)
                assess_2 = np.clip(assess_2, 0, 100)
                
                # Assessment 3: More improvement if intervention
                assess_3 = assess_1 + intervention_effect + np.random.normal(0, 10)
                assess_3 = np.clip(assess_3, 0, 100)
                
                # Assessment 4: Sustained improvement or decline
                trend = (assess_3 - assess_1) / 2  # Half the trend continues
                assess_4 = assess_3 + trend + np.random.normal(0, 12)
                assess_4 = np.clip(assess_4, 0, 100)
                
                # Store assessments
                profile[f'subject_{subject_num}_assess_1'] = round(assess_1, 2)
                profile[f'subject_{subject_num}_assess_2'] = round(assess_2, 2)
                profile[f'subject_{subject_num}_assess_3'] = round(assess_3, 2)
                if subject_num == 3:
                    # Original data has 'subject_4_assess_4' for subject 3's 4th assessment
                    profile['subject_4_assess_4'] = round(assess_4, 2)
                else:
                    profile[f'subject_{subject_num}_assess_4'] = round(assess_4, 2)
                
                # Add empty subject grade (as in original data)
                profile[f'subject_{subject_num}'] = None
        
        print("✓ Generated academic performance data with realistic patterns")
        return profiles
        
    def generate_attendance_patterns(self, profiles):
        """Generate attendance patterns correlated with risk levels"""
        
        for profile in profiles:
            risk_level = profile['risk_level']
            
            # Attendance distributions by risk level (research-backed)
            attendance_params = {
                'low_risk': {'mean': 90, 'std': 8},       # 85-95% average
                'medium_risk': {'mean': 77, 'std': 10},   # 70-85% average
                'high_risk': {'mean': 60, 'std': 12},     # 50-70% average
                'critical_risk': {'mean': 35, 'std': 15}  # <50% average
            }
            
            params = attendance_params[risk_level]
            
            # Attendance_1 is most critical (first 3 weeks rule)
            attendance_1 = np.random.normal(params['mean'], params['std'])
            attendance_1 = np.clip(attendance_1, 0, 100)
            
            # Attendance patterns show decline for high-risk students
            decline_factor = {
                'low_risk': 0.98,      # Slight decline
                'medium_risk': 0.95,   # Moderate decline
                'high_risk': 0.90,     # Significant decline
                'critical_risk': 0.85  # Major decline
            }
            
            # Attendance 2: Shows decline pattern
            attendance_2 = attendance_1 * decline_factor[risk_level] + np.random.normal(0, 5)
            attendance_2 = np.clip(attendance_2, 0, 100)
            
            # Attendance 3: Further decline
            attendance_3 = attendance_2 * decline_factor[risk_level] + np.random.normal(0, 6)
            attendance_3 = np.clip(attendance_3, 0, 100)
            
            # Store attendance
            profile['attendance_1'] = int(round(attendance_1))
            profile['attendance_2'] = int(round(attendance_2))
            profile['attendance_3'] = int(round(attendance_3))
        
        print("✓ Generated attendance patterns with risk-based correlations")
        return profiles
        
    def generate_behavioral_indicators(self, profiles):
        """Generate behavioral indicators and platform issues"""
        
        for profile in profiles:
            risk_level = profile['risk_level']
            
            # Platform access issues probability by risk level
            access_prob = {
                'low_risk': 0.25,      # 25% have access issues
                'medium_risk': 0.35,   # 35% have access issues  
                'high_risk': 0.50,     # 50% have access issues
                'critical_risk': 0.70  # 70% have access issues
            }
            
            # Generate learn_jcu_issues for each subject
            for subject_num in range(1, 4):
                if np.random.random() < access_prob[risk_level]:
                    profile[f'learn_jcu_issues_{subject_num}'] = 'No Access'
                else:
                    profile[f'learn_jcu_issues_{subject_num}'] = 'Access'
            
            # Lecturer referral patterns based on performance and attendance
            referral_categories = ['Attendance', 'Non Submission', 'Concern for Welfare']
            
            for subject_num in range(1, 4):
                attendance = profile[f'attendance_{subject_num}']
                assessment_score = profile[f'subject_{subject_num}_assess_1']
                
                # Determine referral type based on patterns
                if attendance < 50:
                    referral_type = 'Attendance'
                elif assessment_score < 30:
                    referral_type = 'Non Submission'
                elif risk_level in ['high_risk', 'critical_risk']:
                    referral_type = 'Concern for Welfare'
                else:
                    referral_type = np.random.choice(referral_categories)
                
                profile[f'lecturer_referral_{subject_num}'] = referral_type
        
        print("✓ Generated behavioral indicators and platform issues")
        return profiles
        
    def generate_text_fields(self, profiles):
        """Generate realistic text fields (comments and identified issues)"""
        
        # Sample comments for different risk levels and situations
        comments_templates = {
            'low_risk': [
                "Week 3. Student performing well. Consistent attendance and engagement.",
                "Week 5. Good progress on assessments. No concerns identified.",
                "Week 7. Student maintaining good academic standards.",
                "Week 8. Strong performance across all subjects. No intervention needed."
            ],
            'medium_risk': [
                "Week 4. Student submitted first assessment late. Offered academic skills support and advised on extension procedures.",
                "Week 6. Student submitted assessment late. Extension not requested in advance. Advised to submit future requests on time and referred to Academic Skills team.",
                "Week 5. Low engagement in tutorials. Follow-up email sent with participation expectations and links to recorded sessions.",
                "Week 7. Missed second assessment. Student contacted and reported feeling overwhelmed. Referred to Academic Support and encouraged to speak with Counsellor."
            ],
            'high_risk': [
                "Week 3. Student enrolled late. Missing foundational content from Weeks 1–2. Provided links to recorded lectures and encouraged to attend tutorials for extra support.",
                "Week 5. Student absent from multiple classes. Email sent to check in; student replied citing family issues. Offered flexibility and reminded of support services.",
                "Week 6. Student reported working long hours. Referred to careers support for managing work–study balance.",
                "Week 7. Student disclosed high stress levels and lack of sleep. Referred to Wellbeing team and reminded of available mental health support."
            ],
            'critical_risk': [
                "Week 2. Student did not attend orientation. Contacted via email with essential course info and Moodle access guide. No response yet.",
                "Week 3. First contact made. Student reported internet access issues at home. IT support referral provided.",
                "Week 3 late enrolment. Student finding it difficult to catch up on Weeks 1 and 2. Week 4. Student contacted on lecturer referral. Student has been sick on arrival.",
                "booked to see a doctor. Week 5. Student contacted for low attendance. Reminded of the importance of attending classes. Week 7. Student contacted for missing submission due date. Referred to Counsellor for check in for wellbeing as the student advised mental health challenges."
            ]
        }
        
        identified_issues_templates = {
            'low_risk': ['Academic progression', 'Time management', 'Study skills'],
            'medium_risk': ['Poor time management', 'Study skills', 'Late enrollment'],
            'high_risk': ['Mental health', 'Poor time management', 'Late enrollment', 'Financial stress'],
            'critical_risk': ['Mental health', 'Sickness', 'Death in family', 'Late enrollment', 'Financial stress']
        }
        
        for profile in profiles:
            risk_level = profile['risk_level']
            
            # Generate realistic comments
            profile['comments'] = np.random.choice(comments_templates[risk_level])
            
            # Generate identified issues
            profile['identified_issues'] = np.random.choice(identified_issues_templates[risk_level])
        
        print("✓ Generated realistic text fields")
        return profiles
        
    def generate_core_profiles(self):
        """Generate core student profiles with risk-based distribution"""
        
        print("=== GENERATING CORE STUDENT PROFILES ===")
        
        # Step 1: Assign risk levels
        risk_levels = self.assign_risk_levels()
        
        # Step 2: Generate basic profiles
        profiles = self.generate_basic_profiles(risk_levels)
        
        # Step 3: Generate support system data
        profiles = self.generate_support_system_data(profiles)
        
        # Step 4: Generate academic performance
        profiles = self.generate_academic_performance(profiles)
        
        # Step 5: Generate attendance patterns
        profiles = self.generate_attendance_patterns(profiles)
        
        # Step 6: Generate behavioral indicators
        profiles = self.generate_behavioral_indicators(profiles)
        
        # Step 7: Generate text fields
        profiles = self.generate_text_fields(profiles)
        
        print(f"✓ Generated {len(profiles)} complete core profiles")
        return profiles
        
    def validate_data_quality(self, profiles):
        """Validate data quality and consistency"""
        
        print("=== DATA VALIDATION AND QUALITY CONTROL ===")
        
        # Convert to DataFrame for easier analysis
        df = pd.DataFrame(profiles)
        
        # Validation 1: Check attendance-grade correlation
        correlation = df['attendance_1'].corr(df['subject_1_assess_1'])
        print(f"✓ Attendance-grade correlation: {correlation:.3f} (target: ~0.44)")
        
        # Validation 2: Check risk distribution
        risk_counts = df['risk_level'].value_counts()
        print(f"✓ Risk distribution:")
        for risk, count in risk_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {risk}: {count} ({percentage:.1f}%)")
            
        # Validation 3: Check academic status mapping
        print(f"✓ Academic status by risk level:")
        status_risk = df.groupby('risk_level')['academic_status'].value_counts()
        print(status_risk)
        
        # Validation 4: Check support system logic
        high_risk_students = df[df['risk_level'].isin(['high_risk', 'critical_risk'])]
        support_rate = (high_risk_students['follow_up'] == 'Yes').mean()
        print(f"✓ High-risk students receiving follow-up: {support_rate:.1%}")
        
        # Validation 5: Check assessment progression
        print(f"✓ Assessment score progression (Subject 1):")
        print(f"  Assess 1 mean: {df['subject_1_assess_1'].mean():.1f}")
        print(f"  Assess 2 mean: {df['subject_1_assess_2'].mean():.1f}")
        print(f"  Assess 3 mean: {df['subject_1_assess_3'].mean():.1f}")
        print(f"  Assess 4 mean: {df['subject_1_assess_4'].mean():.1f}")
        
        # Validation 6: Check missing data patterns
        print(f"✓ Missing data patterns:")
        print(f"  Failed subjects missing: {df['failed_subjects'].isnull().sum()}/{len(df)} ({df['failed_subjects'].isnull().mean():.1%})")
        print(f"  Study skills missing: {df['study_skills(attended)'].isnull().sum()}/{len(df)} ({df['study_skills(attended)'].isnull().mean():.1%})")
        print(f"  Referral missing: {df['referral'].isnull().sum()}/{len(df)} ({df['referral'].isnull().mean():.1%})")
        
        return df
        
    def export_to_csv(self, df, filename="synthetic_student_data.csv"):
        """Export synthetic data to CSV matching original format"""
        
        print("=== EXPORTING SYNTHETIC DATASET ===")
        
        # Remove the risk_level column (internal use only)
        df_export = df.drop('risk_level', axis=1)
        
        # Reorder columns to match original dataset
        original_columns = [
            'student_id', 'course', 'student_cohort', 'academic_status', 'failed_subjects',
            'study_skills(attended)', 'referral', 'pp_meeting', 'self_assessment',
            'readiness_assessment_results', 'follow_up', 'follow_up_type',
            'subject_1', 'subject_1_assess_1', 'subject_1_assess_2', 'subject_1_assess_3', 'subject_1_assess_4',
            'attendance_1', 'learn_jcu_issues_1', 'lecturer_referral_1',
            'subject_2', 'subject_2_assess_1', 'subject_2_assess_2', 'subject_2_assess_3', 'subject_2_assess_4',
            'attendance_2', 'learn_jcu_issues_2', 'lecturer_referral_2',
            'subject_3', 'subject_3_assess_1', 'subject_3_assess_2', 'subject_3_assess_3', 'subject_4_assess_4',
            'attendance_3', 'learn_jcu_issues_3', 'lecturer_referral_3',
            'comments', 'identified_issues'
        ]
        
        # Note: Original has 'subject_4_assess_4' instead of 'subject_3_assess_4' - keeping original format
        df_export = df_export.reindex(columns=original_columns)
        
        # Export to CSV
        df_export.to_csv(filename, index=False)
        print(f"✓ Exported {len(df_export)} records to {filename}")
        print(f"✓ Dataset shape: {df_export.shape}")
        
        return df_export
        
    def generate_full_dataset(self, n_students=2000):
        """Generate complete synthetic dataset with validation"""
        
        print(f"=== GENERATING FULL SYNTHETIC DATASET ({n_students} students) ===")
        
        # Update number of students
        self.n_students = n_students
        
        # Generate profiles
        profiles = self.generate_core_profiles()
        
        # Validate data quality
        df = self.validate_data_quality(profiles)
        
        # Export to CSV
        df_export = self.export_to_csv(df)
        
        return df_export

if __name__ == "__main__":
    # Test with small sample first
    print("=== TESTING WITH SMALL SAMPLE ===")
    generator = SyntheticStudentDataGenerator(n_students=100)
    df_test = generator.generate_full_dataset(n_students=100)
    
    print("\n=== SAMPLE RECORDS ===")
    print(df_test.head(3).to_string())