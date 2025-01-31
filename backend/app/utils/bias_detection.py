def detect_bias(data):
    # Example: Check for bias in patient data
    if 'gender' in data and data['gender'] not in ['male', 'female', 'other']:
        return True
    return False