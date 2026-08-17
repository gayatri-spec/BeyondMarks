import pandas as pd

# Load O*NET transferable skills
skills_df = pd.read_csv(
    "../data/raw/transferable_skills.csv"
)

# Career codes
careers = {
    "Business Intelligence Analyst": "15-2051.01",
    "Data Scientist": "15-2051.00",
    "Operations Research Analyst": "15-2031.00",
    "Computer Systems Analyst": "15-1211.00"
}

print("\n===== CAREER TRANSFERABLE SKILLS =====")

for career, code in careers.items():

    career_data = skills_df[
        skills_df["O*NET-SOC Code"] == code
    ]

    # Remove duplicate skill names
    result = career_data[
        ["Element Name", "Scale Name", "Data Value"]
    ].drop_duplicates()

    print(f"\n{career}")
    print("-" * len(career))

    print(
        f"{'Skill':<35}"
        f"{'Scale':<10}"
        f"{'Value':<10}"
    )

    print("-" * 55)

    for _, row in result.head(15).iterrows():

        print(
            f"{str(row['Element Name']):<35}"
            f"{str(row['Scale Name']):<10}"
            f"{str(row['Data Value']):<10}"
        )
print("\n===== DATA SCIENTISTS CHECK =====\n")

data_scientists = skills_df[
    skills_df["Title"].str.strip().str.lower() == "data scientists"
]

if data_scientists.empty:
    print("Data Scientists not found in transferable skills data.")
else:
    print("Data Scientists found!")

    print(
        f"{'Code':<15}"
        f"{'Title':<25}"
        f"{'Skill':<35}"
        f"{'Scale':<12}"
        f"{'Value':<10}"
    )

    print("-" * 97)

    for _, row in data_scientists.head(20).iterrows():
        print(
            f"{str(row['O*NET-SOC Code']):<15}"
            f"{str(row['Title']):<25}"
            f"{str(row['Element Name']):<35}"
            f"{str(row['Scale Name']):<12}"
            f"{str(row['Data Value']):<10}"
        )


