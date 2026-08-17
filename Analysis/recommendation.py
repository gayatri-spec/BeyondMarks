import pandas as pd

# ==========================================
# BEYONDMARKS - FINAL CAREER RECOMMENDATION
# ==========================================

# Load O*NET software data
software_df = pd.read_csv(
    "../data/raw/software_skills.csv"
)

# Career codes
careers = {
    "Business Intelligence Analyst": "15-2051.01",
    "Data Scientist": "15-2051.00",
    "Operations Research Analyst": "15-2031.00",
    "Computer Systems Analyst": "15-1211.00"
}

# ------------------------------------------------
# Student Information
# ------------------------------------------------

student_skills = [
    "Microsoft Excel",
    "Microsoft Power BI",
    "Python",
    "SQL"
]

student_profile = "Developing Potential"

profile_bonus = {
    "Strong Learner": 10,
    "Developing Potential": 5,
    "Balanced": 0
}

bonus = profile_bonus[student_profile]

# Relevant technologies
technology_list = [
    "Microsoft Excel",
    "Microsoft Power BI",
    "Tableau",
    "Python",
    "R",
    "SAS",
    "Alteryx",
    "MATLAB",
    "SPSS",
    "Hadoop",
    "Spark",
    "AWS",
    "Azure"
]

# ==========================================
# CAREER MATCHING
# ==========================================

results = []

for career, code in careers.items():

    career_data = software_df[
        software_df["O*NET-SOC Code"] == code
    ].copy()

    # Keep only relevant technologies
    career_data = career_data[
        career_data["Workplace Example"].isin(
            technology_list
        )
    ]

    # Remove duplicates
    career_data = career_data.drop_duplicates(
        subset=["Workplace Example"]
    )

    total_weight = 0
    matched_weight = 0

    matching_skills = []
    missing_skills = []

    student_lower = [
        skill.lower()
        for skill in student_skills
    ]

    for _, row in career_data.iterrows():

        technology = str(
            row["Workplace Example"]
        )

        hot = str(
            row["Hot Technology"]
        ).upper()

        demand = str(
            row["In Demand"]
        ).upper()

        # Weight according to O*NET
        if hot == "Y" and demand == "Y":
            weight = 3

        elif hot == "Y" or demand == "Y":
            weight = 2

        else:
            weight = 1

        total_weight += weight

        if technology.lower() in student_lower:

            matched_weight += weight
            matching_skills.append(
                technology
            )

        else:
            missing_skills.append(
                technology
            )

    # Calculate skill score
    if total_weight > 0:

        skill_score = (
            matched_weight /
            total_weight
        ) * 100

    else:
        skill_score = 0

    # Add learning profile
    final_score = min(
        skill_score + bonus,
        100
    )

    results.append({
        "career": career,
        "skill_score": skill_score,
        "final_score": final_score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    })


# ==========================================
# SORT CAREERS
# ==========================================

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)


# ==========================================
# FINAL BEYONDMARKS REPORT
# ==========================================

print("\n")
print("=" * 55)
print("              BEYONDMARKS")
print("        CAREER RECOMMENDATION REPORT")
print("=" * 55)

print("\nSTUDENT PROFILE")
print("-" * 55)

print(
    f"Learning Profile : {student_profile}"
)

print(
    "Current Skills   : "
    + ", ".join(student_skills)
)


# ==========================================
# TOP CAREERS
# ==========================================

print("\nTOP CAREER RECOMMENDATIONS")
print("-" * 55)

for i, result in enumerate(
    results[:3],
    start=1
):

    print(
        f"{i}. {result['career']:<35}"
        f"{result['final_score']:.1f}%"
    )


# ==========================================
# DETAILED TOP CAREER
# ==========================================

top = results[0]

print("\n")
print("=" * 55)
print("             BEST CAREER MATCH")
print("=" * 55)

print(
    f"\nCareer       : {top['career']}"
)

print(
    f"Skill Match  : {top['skill_score']:.1f}%"
)

print(
    f"Final Score  : {top['final_score']:.1f}%"
)


print("\nMATCHING SKILLS")
print("-" * 55)

if top["matching_skills"]:

    for skill in top["matching_skills"]:
        print(f"✓ {skill}")

else:
    print("No matching skills found.")


print("\nRECOMMENDED SKILLS TO LEARN")
print("-" * 55)

if top["missing_skills"]:

    for skill in top["missing_skills"][:5]:
        print(f"→ {skill}")

else:
    print("No major skill gaps found.")


print("\n")
print("=" * 55)
print("          END OF BEYONDMARKS REPORT")
print("=" * 55)