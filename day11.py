def vaccination_schedule(age_months):
    # Detailed Vaccination schedule based on age in months
    schedule = []
    
    if age_months == 0:
        schedule.append("At birth: Colostrum from mother's milk (for natural immunity).")
    
    if 6 <= age_months <= 8:
        schedule.append("6-8 weeks: First DHPP vaccine (Distemper, Hepatitis, Parainfluenza, Parvovirus).")
    
    if 10 <= age_months <= 12:
        schedule.append("10-12 weeks: Second DHPP vaccine, Bordetella vaccine (Kennel Cough), and Rabies vaccine.")
    
    if 14 <= age_months <= 16:
        schedule.append("14-16 weeks: Third DHPP vaccine, Leptospirosis vaccine, and Lyme disease vaccine (if applicable).")
    
    if age_months == 52:
        schedule.append("1 year: DHPP and Rabies booster, Bordetella booster, and optional Canine Influenza vaccine.")
    
    if 104 <= age_months <= 156:
        schedule.append("2-3 years: Annual DHPP booster, Rabies booster every 3 years, and optional Leptospirosis booster.")
    
    if 208 <= age_months <= 240:
        schedule.append("4-5 years: Annual DHPP booster, Rabies booster every 3 years, and optional Lyme disease booster.")
    
    if 312 <= age_months <= 480:
        schedule.append("6-8 years: DHPP and Rabies boosters as needed, and continued annual or bi-annual check-ups.")
    
    if 600 <= age_months <= 720:
        schedule.append("10-12 years: Continue age-appropriate vaccinations based on veterinarian recommendation.")
    
    if 840 <= age_months <= 960:
        schedule.append("14-15 years: Monitor closely for health changes, minimal vaccinations as recommended by veterinarian.")

    return schedule

def deworming_schedule(age_months):
    # Deworming schedule
    if age_months <= 6:
        return "Deworm every 2 weeks until 6 months old."
    elif age_months <= 12:
        return "Deworm once a month until 12 months old."
    elif age_months <= 156:
        return "Deworm every 3-6 months after 12 months old."
    else:
        return "Deworm every 6-12 months depending on health and environment."

def health_problems(age_months):
    # Health problems and treatments
    health_issues = {
        "Viral Fever": "Treatment: Antiviral medications like amantadine, and supportive care with fluids and rest.",
        "Heart Issues": "Treatment: Medications such as ACE inhibitors, Beta-blockers, and diuretics. Regular monitoring is crucial.",
        "External/Internal Injuries (e.g., Fracture)": "Treatment: Pain management with analgesics, anti-inflammatory drugs, and surgery if necessary."
    }

    return health_issues

def main():
    # Input Dog's name and age
    dog_name = input("Enter your dog's name: ")
    age_years = int(input("Enter your dog's age in years: "))
    age_months = age_years * 12
    
    # Display vaccination schedule
    print(f"\nVaccination Schedule for {dog_name}:")
    for vaccine in vaccination_schedule(age_months):
        print(vaccine)
    
    # Display deworming schedule
    print(f"\nDeworming Schedule for {dog_name}:")
    print(deworming_schedule(age_months))
    
    # Display common health issues and treatments
    print(f"\nCommon Health Problems for {dog_name}:")
    for problem, treatment in health_problems(age_months).items():
        print(f"{problem}: {treatment}")

if __name__ == "__main__":
    main()
