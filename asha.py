import json
import difflib
import textwrap

# Sample data simulating offline storage
SYMPTOM_RISK_DB = {
    "bleeding": "High-risk pregnancy. Immediate referral suggested.",
    "severe headache": "May indicate high blood pressure. Monitor closely.",
    "swelling": "Possible preeclampsia. Recommend further testing.",
    "low hemoglobin": "Anemia detected. Iron and folic acid required.",
    "underweight child": "Needs nutrition support. Start supplementary diet.",
}

SCHEME_DB = [
    {"name": "Janani Suraksha Yojana", "target": "Pregnant Women", "income": "BPL", "state": "ALL"},
    {"name": "PM Jan Arogya Yojana", "target": "Families", "income": "BPL", "state": "ALL"},
    {"name": "Matru Vandana Yojana", "target": "Pregnant Women", "income": "ALL", "state": "ALL"},
]

DIET_SUGGESTIONS = {
    "Uttar Pradesh": {
        "anemia": ["Jaggery", "Spinach", "Lentils", "Amla", "Bajra Roti"],
        "underweight": ["Banana", "Khichdi", "Boiled potatoes", "Ghee roti"]
    }
}

wrapper = textwrap.TextWrapper(width=70)

def check_risk(symptom):
    matches = difflib.get_close_matches(symptom.lower(), SYMPTOM_RISK_DB.keys(), n=1)
    if matches:
        return SYMPTOM_RISK_DB[matches[0]]
    return "Symptom not recognized. Please consult a doctor."

def scheme_checker(state, income, person):
    eligible = []
    for scheme in SCHEME_DB:
        if (scheme["state"] == "ALL" or scheme["state"] == state) and \
           (scheme["income"] == "ALL" or scheme["income"] == income) and \
           (scheme["target"] in person):
            eligible.append(scheme["name"])
    return eligible

def get_diet(state, condition):
    return DIET_SUGGESTIONS.get(state, {}).get(condition, ["Diet info not available."])

def ai_assistant():
    print("\n👩‍⚕ Welcome to ASHA Assistant\n")
    name = input("Enter patient name: ")
    state = input("Enter state: ")
    income = input("Income group (APL/BPL): ")
    person = input("Patient is (Pregnant Woman / Child / Family): ")

    print("\n🔍 Enter symptom for risk detection (e.g., 'swelling', 'low hemoglobin'):")
    symptom = input("> ")
    print("\n🩺 Risk Detection:")
    print(wrapper.fill(check_risk(symptom)))

    print("\n🍱 Dietary Suggestion:")
    condition = "anemia" if "hemoglobin" in symptom else "underweight" if "underweight" in symptom else "general"
    print(", ".join(get_diet(state, condition)))

    print("\n🏥 Eligible Healthcare Schemes:")
    schemes = scheme_checker(state, income.upper(), person)
    if schemes:
        for s in schemes:
            print(f"✔ {s}")
    else:
        print("No schemes found for given details.")

    print("\n📁 Patient Record Saved Locally (Simulation).\n")

if _name_ == "_main_":
    ai_assistant()
