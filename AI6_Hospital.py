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

'''
class Employee: 
def __init__(self, name, productivity, communication, teamwork, initiative): 
self.name = name 
self.productivity = productivity 
self.communication = communication 
self.teamwork = teamwork 
self.initiative = initiative 
class PerformanceEvaluator: 
def __init__(self): 
self.criteria_weights = { 
"productivity": 0.4, 
"communication": 0.3, 
"teamwork": 0.2, 
"initiative": 0.1 
} 
def evaluate(self, employee): 
score = 0 
for criterion, weight in self.criteria_weights.items(): 
score += getattr(employee, criterion) * weight 
if score >= 0.8: 
return f"{employee.name} has excellent performance." 
elif score >= 0.6: 
return f"{employee.name} has good performance." 
elif score >= 0.4: 
return f"{employee.name} has satisfactory performance." 
else: 
return f"{employee.name} needs improvement in performance." 
# Example usage 
employee1 = Employee("Employee A", 0.4, 0.6, 0.3, 0.2) 
employee2 = Employee("Employee B", 0.6, 0.8, 0.7, 0.5) 
evaluator = PerformanceEvaluator() 
print(evaluator.evaluate(employee1)) 
print(evaluator.evaluate(employee2)) 
 
 
 
 
 
 
'''
