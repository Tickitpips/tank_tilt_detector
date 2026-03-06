import joblib

def load_tilt_model():

    model = joblib.load("saved_models/tilt_random_forest.pkl")

    return model