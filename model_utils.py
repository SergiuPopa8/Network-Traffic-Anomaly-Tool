import joblib
from sklearn.ensemble import RandomForestClassifier
from config import MODEL_PATH

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    return joblib.load(MODEL_PATH)
