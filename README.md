# ScoreSync

### Student Performance Intelligence

> An ML-powered academic performance prediction system for estimating semester SPI, overall CGPA, and academic risk.

---

## 📌 Overview

**ScoreSync** is a machine learning-based student performance prediction system designed to analyze academic and study-related factors and provide an early indication of a student's expected academic performance.

The system uses student information such as previous CGPA, attendance, internal marks, assignment performance, practical scores, study hours, class participation, and backlogs to generate performance predictions.

ScoreSync combines a machine learning backend with an interactive **Gradio dashboard**, allowing users to enter their academic information and instantly view their predicted performance.

---

## 🎯 Objectives

- Predict a student's current semester **SPI**
- Estimate **overall CGPA**
- Identify the student's **academic status**
- Detect potential **academic risk**
- Provide an easy-to-use academic performance dashboard
- Maintain a history of previous predictions

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎓 SPI Prediction | Predicts current semester performance |
| 📊 CGPA Prediction | Estimates overall academic CGPA |
| ⚠️ Risk Detection | Identifies students potentially at academic risk |
| 👤 Authentication | Student registration and login |
| 📈 Prediction History | Stores previous prediction results |
| 🖥️ Interactive Dashboard | Simple web interface using Gradio |
| 🏫 Engineering Support | Designed around engineering academic parameters |

---

## 🧠 Machine Learning

ScoreSync uses machine learning techniques for two major tasks:

### Regression

Used to predict continuous academic values such as:

- Semester SPI
- Overall CGPA

### Classification

Used to determine:

- Academic Status
- Academic Risk

The project includes preprocessing and trained machine learning models using **Scikit-learn**.

---

## 📥 Input Parameters

The prediction system considers multiple academic and study-related factors:

- Engineering Branch
- Current Semester
- Age
- Gender
- Previous CGPA
- Attendance
- Internal Marks
- Assignment Score
- Practical Score
- Current Backlogs
- Study Hours per Day
- Classes Attended
- Assignment Completion

---

## 🔄 System Workflow

```text
┌──────────────────────┐
│       Student        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Login / Registration│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Enter Academic Data  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Data Preprocessing   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Machine Learning     │
│       Models         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ SPI / CGPA / Status  │
│      Prediction      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Prediction History   │
└──────────────────────┘
