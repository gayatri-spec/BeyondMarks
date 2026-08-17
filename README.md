# BeyondMarks

### Explainable Career Recommendation System

> **Go Beyond Marks. Discover Your Potential.**

## 📌 About the Project

BeyondMarks is a data-driven and explainable career recommendation system that goes beyond academic marks.

It analyzes:
- Academic performance
- Learning behavior
- Student skills
- O*NET occupational technology requirements

The system generates a **Career Match Score**, recommends suitable careers, and identifies skills that students can learn next.

## 🎯 Problem Statement

Students are often evaluated mainly through academic marks. However, marks alone may not represent a student's learning behavior, practical skills, strengths, or career readiness.

BeyondMarks aims to provide a more holistic and explainable approach to career guidance.

## 💡 Proposed Solution

The system combines student academic and learning indicators with current technical skills and O*NET career technology data.

### Workflow

Student Data  
↓  
Data Cleaning & EDA  
↓  
Academic & Learning Analysis  
↓  
Learning Profile  
↓  
Student Skills  
↓  
O*NET Career Data  
↓  
Skill Matching & Scoring  
↓  
Career Recommendations  
↓  
Skill Gap Suggestions

## 📊 Dataset

### Student Dataset
- 395 student records
- Academic grades
- Study time
- Absences
- Previous failures
- Activities and support indicators

### O*NET Data
- Occupation titles
- Workplace technologies
- Hot Technology indicators
- In-Demand technology indicators

## 🧠 Career Matching

The prototype compares student skills with relevant career technologies.

Technology requirements are weighted using O*NET indicators such as:
- Hot Technology
- In Demand

The result is an explainable **Career Match Score**.

## 📈 Sample Result

### Top Career Recommendations

1. **Computer Systems Analyst — 65.0%**
2. **Operations Research Analyst — 61.2%**
3. **Business Intelligence Analyst — 55.0%**

### Current Skills
- Microsoft Excel
- Microsoft Power BI
- Python
- SQL

### Example Skills to Learn
- R
- SAS
- Tableau

> Career Match Score is an explainable prototype score, not job-placement probability.

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- O*NET Occupational Data
- Jupyter Notebook
- VS Code

## 🚀 Future Scope

- Student-facing web dashboard
- ML-based personalized recommendations
- Personalized learning resources
- Skill development tracking
- More career domains

## 👩‍💻 Project

**BeyondMarks — Hackathon Project**

Built as a prototype for explainable, data-driven career guidance.
