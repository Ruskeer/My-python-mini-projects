import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# This function evaluates whether individual record fields meet specific requirements.
# It returns a list containing ONLY the field names (keys) that failed validation.
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):

    # This dictionary maps each field to a Boolean indicating if its contents are valid.
    constraints = {
        # Validates that 'patient_id' is a string matching 'p' followed strictly by digits.
        'patient_id': isinstance(patient_id, str) and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        
        # Validates that 'age' is an integer and is at least 18.
        'age' : isinstance(age, int) and age >= 18,
        
        # Validates that 'gender' is a string and matches either 'male' or 'female' (case-insensitive).
        'gender': isinstance(gender, str) and gender.lower() in ('male','female'),
        
        # Validates that 'diagnosis' is either a valid string or an empty field (None).
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # CRITICAL CORRECTION (CLEARLINES): Added 'all()'. Without 'all()', a non-empty list of validation 
        # results like [False, False] evaluates to a Truthy value, completely bypassing validation.
        'medications' : isinstance(medications, list) and all([isinstance(i, str) for i in medications]),
        
        # Validates that 'last_visit_id' is a string matching 'v' followed strictly by digits.
        'last_visit_id' : isinstance(last_visit_id, str) and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }

    # CRITICAL CORRECTION (CLEARLINES): Added 'if not value' filtering.
    # Your original code returned ALL keys unconditionally, making valid fields report as errors.
    return [key for key, value in constraints.items() if not value]
    
def validate(data):
    # Verifies that the top-level container structure is either a tuple or a list.
    is_sequence = isinstance(data, (tuple, list))

    # Halts execution and signals a structural failure if the top-level collection is incorrect.
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False

    is_invalid = False

    # CLEARLINES: Sets do not enforce order. This set acts as a comprehensive checklist.
    # It ensures every dictionary has all required keys and contains no extraneous keys.
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # Loops over the data collection tracking both index positions and contents.
    for index, dictionary in enumerate(data):
        # Enforces that every record structure within the sequence must be a Python dictionary.
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
            continue

        # CLEARLINES: 'set(dictionary)' extracts keys only. This structural comparison 
        # matches the keys present in the data record against the standard key checklist set.
        if set(dictionary) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue

        # CLEARLINES: '**dictionary' unpacks key-value pairs as individual keyword arguments.
        # This matches keys like 'patient_id' directly into the function arguments.
        invalid_records = find_invalid_records(**dictionary)

        # Loops through the failed field keys returned from the constraints function.
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    # Triggers a broad failure state if any record structural format or internal constraint failed.
    if is_invalid:
        return False

    # Executes only if every structural check and data value constraint successfully passes validation.
    print("Valid Format")
    return True

validate(medical_records)
