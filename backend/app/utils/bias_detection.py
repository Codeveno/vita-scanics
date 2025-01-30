def detect_bias(data):
    if 'gender' in data:
        return "Potential bias detected"
    return "No bias detected"
