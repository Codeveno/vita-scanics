def validate_patient_data(data):
    required_fields = ['patient_id', 'symptoms']
    for field in required_fields:
        if field not in data:
            return False
    return True