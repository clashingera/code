symptoms = ["Fever", "Cough", "Headache", "Sore throat"]

diseases = {
    "Common Cold": ["Fever", "Cough", "Headache", "Sore throat"],
    "Flu": ["Fever", "Cough", "Headache"],
    "Strep Throat": ["Fever", "Sore throat"],
    "Migraine": ["Headache"]
}


def get_user_input():
    user_symptoms = []
    for symptom in symptoms:
        response = input(f"Do you have {symptom}? (y/n): ")
        if response.lower() == 'y':
            user_symptoms.append(symptom)
    return user_symptoms


def diagnose():
    user_symptoms = get_user_input()
    possible_diseases = set()
    for symptom in user_symptoms:
        for disease, causes in diseases.items():
            if symptom in causes:
                possible_diseases.add(disease)

    if possible_diseases:
        print("Possible diseases:")
        for disease in possible_diseases:
            print("- " + disease)
    else:
        print("No matching diseases found.")


def main():
    print("Welcome to Symptom Checker")
    print("You can start by answering some questions about your symptoms.")
    diagnose()


if __name__ == "__main__":
    main()