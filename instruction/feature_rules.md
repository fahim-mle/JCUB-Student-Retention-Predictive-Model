# Academic Risk Prediction Dataset: Feature Analysis & Rules

## **SYNTHETIC DATA GENERATION PRINCIPLES**

Based on research findings and real-world student patterns:

### **Risk Distribution (Based on Client's 300/2000 students needing support)**

- **Low Risk**: 60% - Good attendance (>85%), grades (>65%), minimal support needs
- **Medium Risk**: 25% - Moderate attendance (70-85%), grades (50-65%), some support utilization
- **High Risk**: 12% - Poor attendance (<70%), grades (<50%), multiple interventions
- **Critical Risk**: 3% - Multiple failures, unresponsive, major barriers

### **Temporal Patterns**

- **Week 1-3**: Critical prediction period (78% accuracy for semester outcome)
- **Week 4-8**: Optimal intervention window
- **Assessment 1**: Primary predictor of final performance
- **Support Timing**: Earlier intervention = better outcomes

### **Real-world Biases to Include**

- STEM courses: Higher early failure rates
- International students: Language barriers, cultural adjustment
- Financial stress: Irregular attendance, work conflicts
- Mental health issues: Declining engagement patterns
- Support paradox: Struggling students have more support data

## **FEATURE ANALYSIS TABLE**

| Feature Name | Variable Type | Initial Values/Range | Proposed Values/Range |
|--------------|---------------|---------------------|----------------------|
| student_id | Integer | 1-99999 | N/A |
| course | Categorical | Engineering, Business, IT, Health Sciences, Arts | N/A |
| student_cohort | Categorical | 2024_S1, 2024_S2, 2025_S1 | N/A |
| academic_status | Categorical | good_standing, monitoring, at_risk, critical | N/A |
| failed_subjects | Categorical | 0, 1, 2, 3+ | N/A |
| study_skills(attended) | Categorical | Yes, No, null | N/A |
| referral | Categorical | Yes, No, null | N/A |
| pp_meeting | Categorical | Yes, No, null | N/A |
| self_assessment | Categorical | Financial stress, Family issues, Mental health, Transport, English difficulties, University expectations, Time management, null | N/A |
| readiness_assessment_results | Categorical | High risk identified, Some concerns, Satisfactory, Excellent preparation | N/A |
| follow_up | Categorical | Yes, No, null | N/A |
| follow_up_type | Categorical | Academic support, Welfare check, Urgent intervention, Administrative, null | N/A |
| subject_1 | Float | 0-100 | N/A |
| subject_1_assess_1 | Float | 0-100 | N/A |
| subject_1_assess_2 | Float | 0-100 | N/A |
| subject_1_assess_3 | Float | 0-100 | N/A |
| subject_1_assess_4 | Float | 0-100 | N/A |
| attendance_1 | Integer | 0-100 | N/A |
| learn_jcu_issues_1 | Categorical | Digital literacy, English language, No laptop, Late submissions, No access >7 days, Technical issues, null | N/A |
| lecturer_referral_1 | Categorical | Yes, No, null | N/A |
| subject_2 | Float | 0-100 | N/A |
| subject_2_assess_1 | Float | 0-100 | N/A |
| subject_2_assess_2 | Float | 0-100 | N/A |
| subject_2_assess_3 | Float | 0-100 | N/A |
| subject_2_assess_4 | Float | 0-100 | N/A |
| attendance_2 | Integer | 0-100 | N/A |
| learn_jcu_issues_2 | Categorical | Digital literacy, English language, No laptop, Late submissions, No access >7 days, Technical issues, null | N/A |
| lecturer_referral_2 | Categorical | Yes, No, null | N/A |
| subject_3 | Float | 0-100 | N/A |
| subject_3_assess_1 | Float | 0-100 | N/A |
| subject_3_assess_2 | Float | 0-100 | N/A |
| subject_3_assess_3 | Float | 0-100 | N/A |
| subject_3_assess_4 | Float | 0-100 | N/A |
| attendance_3 | Integer | 0-100 | N/A |
| learn_jcu_issues_3 | Categorical | Digital literacy, English language, No laptop, Late submissions, No access >7 days, Technical issues, null | N/A |
| lecturer_referral_3 | Categorical | Yes, No, null | N/A |
| comments | String | Free text observations | N/A |
| identified_issues | String | Free text staff notes | N/A |

## **GENERATION RULES SUMMARY**

### **Academic Performance Rules**

- subject_1 typically lowest (foundational filter)
- assess_1 performance predicts 78% of final outcomes
- Students with support show 5-15% improvement over semester
- Grade distribution: 25% high (>75), 50% average (50-75), 25% struggling (<50)

### **Attendance Rules**

- First 3 weeks most critical for prediction
- >95% attendance correlates with A/B grades
- Each 10% attendance drop = ~6-8 grade point decrease
- High-risk students show 15-30% decline pattern

### **Support System Rules**

- 15% of students need intervention (300/2000)
- pp_meeting reserved for 8% highest risk
- Follow-up effectiveness decreases if delayed >2 weeks
- Support paradox: More support data = initially struggling students

### **Behavioral Indicator Rules**

- learn_jcu_issues escalate if unaddressed
- Digital literacy issues correlate with age/background
- Language barriers affect international students primarily
- Issues in multiple subjects indicate critical risk

### **Missing Data Patterns**

- High performers: Sparse support data (no intervention needed)
- Critical risk: Complete monitoring data
- Random technical missing: 2-5% across columns
- Strategic missing: No support needed = null values
