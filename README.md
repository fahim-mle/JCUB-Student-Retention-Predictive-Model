# JCUB Student Success & Retention Predictive Analytics

## 🎯 Project Overview

This project aims to leverage data science to identify factors influencing student success and retention at the James Cook University Brisbane (JCUB) Learning Centre. Our goal is to develop a robust predictive model and generate actionable insights that can help educational institutions proactively support students, thereby improving academic outcomes and reducing dropout rates. This initiative focuses on developing a proof-of-concept system capable of early identification and categorization of "at-risk" students, enabling timely and targeted interventions.

## 💡 Problem Statement

Student attrition presents significant academic and financial challenges for higher education institutions. The JCUB Learning Centre seeks a data-driven approach to move from reactive support to proactive intervention. Currently, student risk identification and support efforts are primarily manual and lack a formal, systematic framework. The objective is to establish a predictive capability that can flag students demonstrating early warning signs, even before formal academic status changes occur.

## 🚧 Challenges & Strategic Approach

A primary challenge for this internship project is the **absence of real student data** from JCUB, with only a simulated dataset provided. This limits the immediate real-world applicability and accuracy of our predictive models. Furthermore, the provided dummy dataset exhibits **structural inconsistencies**, with columns growing dynamically by semester and subject, making it unsuitable for direct Exploratory Data Analysis (EDA) or model training.

To overcome these limitations and deliver a valuable proof-of-concept, our strategy is as follows:

1.  **Leverage Open-Source Data & Research:** We will extensively research existing studies and openly available datasets (e.g., from Kaggle) on student performance and dropout prediction. This will inform our understanding of relevant features, correlations, and successful machine learning algorithms.
2.  **Data Structuring & Cleaning:** We will analyze the provided dummy data to understand its inherent structure and identify necessary transformations. A significant effort will be dedicated to restructuring and cleaning this data to create a suitable foundation for analysis and feature engineering.
3.  **Synthetic Data Generation:** Based on insights derived from academic research and patterns observed (or expected) in educational datasets, we will generate synthetic data. This will allow us to build and validate our predictive models in a controlled environment, demonstrating the methodology and potential insights that could be achieved with real data.
4.  **Proof-of-Concept Predictive Modeling:** Machine learning algorithms (e.g., Random Forest, k-Nearest Neighbors) will be applied to the structured and synthetic datasets to build a predictive model capable of classifying students as "at-risk" or "not at-risk". The model's primary goal will be to identify at-risk students early in their course, ideally by week 4.
5.  **Data Collection Recommendations:** We will formulate concrete recommendations for JCUB on how to standardize and improve their data collection practices to enable the future development of a truly accurate and deployable student success prediction system.

## 📊 Data

The initial dataset provided by JCUB (`jcudata.xlsx - Sheet1.csv`) is a simulated student tracking log. It contains various categories including:
* Student Demographics & Identifiers (e.g., Student ID, Name, Email).
* Enrollment & Status (e.g., Course, Student Cohort, Academic Status).
* Academic Performance & Engagement (e.g., Failed Subjects, Assessment Grades, Attendance, Learn JCU Issues, Lecturer Referrals).
* Intervention & Support Data (e.g., Study Skills, Referrals, PP Meeting, Follow-up).
* Qualitative Contextual Data (e.g., Notes/Comments, Identified Issues).

**Current Data Challenges:**
* **Simulated Records:** All records are fake, limiting real-world validation.
* **Inconsistent Structure:** Subject and assessment columns are repeated and grow with the number of subjects (up to 4 per semester) and assignments (at least 3 per subject), posing significant challenges for direct analysis and feature engineering.
* **Data Quality:** Presence of duplicate columns and inconsistent formats (e.g., mixed dates/scores in assessment columns) require extensive preprocessing.

## 🧪 Methodology

Our project will follow a structured data science methodology:

1.  **Data Ingestion & Initial Assessment:** Load and review the provided dummy dataset, understanding its structure and identifying initial quality issues.
2.  **Data Cleaning & Restructuring:** Implement robust Python scripts to handle missing values, remove redundancies, standardize formats, and pivot the data into a more suitable, normalized structure for analysis (e.g., separate tables for students, subjects, assessments).
3.  **Feature Engineering:** Derive meaningful features from the cleaned data. This will include creating metrics like `Num_Failed_Subjects`, `Avg_Attendance`, `Num_Failed_Assessments`, and binary flags for `Is_Late_Enrolment`, `Has_Wellbeing_Issue`, etc., based on identified risk indicators.
4.  **Synthetic Data Generation:** Develop a methodology to generate a synthetic dataset that mirrors the statistical properties and correlations of key risk factors observed in academic research and the structured dummy data.
5.  **Predictive Model Development:**
    * Define the target variable (e.g., 'at-risk' status based on `Academic Status` or a composite risk score).
    * Train and validate machine learning classification models (e.g., Random Forest, Decision Trees, k-Nearest Neighbors) on the synthetic dataset.
    * Evaluate model performance using appropriate metrics (e.g., accuracy, precision, recall, F1-score).
6.  **Data Visualization & Reporting:** Create interactive dashboards using Power BI to visualize key performance indicators, identified risk factors, and predicted at-risk student profiles. This will allow for flexible reporting filtered by subject, course, risk factors, and academic performance.
7.  **Recommendations:** Provide actionable recommendations for improving student data collection and institutional intervention strategies.

## 📦 Key Deliverables

* **Cleaned & Structured Dataset:** A well-organized, processed version of the simulated data.
* **Synthetic Data Generation Script:** Code to produce a synthetic dataset that mimics real-world student data characteristics.
* **Proof-of-Concept Predictive Model:** A trained and validated machine learning model for identifying at-risk students.
* **Interactive Power BI Dashboard:** Visualizations and summaries of student risk status, enabling exploratory analysis.
* **Comprehensive Project Report:** Detailing methodology, findings, model performance, and recommendations for JCUB.
* **Recommendations for Data Collection:** Guidelines for improving future data acquisition.

## 🛠️ Technical Stack

* **Programming Language:** Python
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (for model implementation)
* **Cloud Platform:** Microsoft Azure (for compute and notebooks)
* **Data Visualization:** Microsoft Power BI
* **Version Control:** Git, GitHub

## 🚀 Getting Started (for local development)

11.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/JCUB-Student-Success-Analytics.git](https://github.com/your-username/JCUB-Student-Success-Analytics.git)
    cd JCUB-Student-Success-Analytics
    ```
2.  **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` will be generated based on the libraries used in the notebooks and scripts.)*
4.  **Access Notebooks:** Navigate to the `notebooks/` directory to explore the data cleaning, feature engineering, and model development steps.

## 📄 Usage

*(Placeholder: Instructions on how to run specific notebooks, scripts, or view Power BI reports locally or online.)*

## 🔮 Future Work & Recommendations for JCUB

* **Integrate Real Data:** The most critical next step is to integrate real, anonymized student data to train and validate truly accurate predictive models.
* **Automate Data Pipelines:** Establish automated data extraction from university systems (SIS, LMS, support logs) to ensure a continuous flow of high-quality data.
* **Standardize Data Collection:** Implement consistent protocols for recording all relevant student data points across departments.
* **Longitudinal Data Tracking:** Capture time-series data more granularly to track student progression and the impact of interventions over time.
* **Intervention Efficacy Measurement:** Design data collection to explicitly track the outcomes and effectiveness of different support interventions.
* **Ethical Considerations:** Continuously review and ensure fairness, privacy, and transparency in the use of predictive analytics for student support.
* **Iterative Model Refinement:** Establish a process for continuous monitoring, feedback, and retraining of the predictive model to maintain relevance and accuracy.

## 🤝 Team

* Molormaa Ch (Research and Development)
* Galey Wangmo (Team Lead and Coordinator)
* Fahim Forhad (Data Exploration and Modeling)
* Buyankhishig M (UI/UX and Communication)
