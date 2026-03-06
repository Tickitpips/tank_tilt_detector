import joblib
from sklearn.ensemble import RandomForestRegressor

def train_random_forest(X_train, y_train):

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "saved_models/tilt_random_forest.pkl")

    return model