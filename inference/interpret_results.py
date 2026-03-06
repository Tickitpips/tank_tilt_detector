def interpret_tilt(k):

    k = abs(k)

    if k < 0.0005:
        status = "Tank is level"
        severity = "None"

    elif k < 0.002:
        status = "Minor tilt detected"
        severity = "Low"

    elif k < 0.005:
        status = "Moderate tilt detected"
        severity = "Medium"

    else:
        status = "Severe tilt detected"
        severity = "High"

    return status, severity