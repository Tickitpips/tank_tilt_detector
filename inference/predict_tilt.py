from models.load_model import load_tilt_model

model = load_tilt_model()

def predict_tilt(features):

    k_pred = model.predict(features)

    return k_pred.mean()