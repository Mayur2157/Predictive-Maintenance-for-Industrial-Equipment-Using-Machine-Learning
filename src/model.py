import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(X, y):
    """
    Train a RandomForest model using the provided features and labels.

    Args:
        X (pd.DataFrame): The input features for the model.
        y (pd.Series): The target labels.

    Returns:
        model (RandomForestClassifier): The trained RandomForest model.
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save the trained model to a file
    joblib.dump(model, '../models/random_forest_model.pkl')

    return model

def predict(model, X_new):
    """
    Make predictions using the trained model.

    Args:
        model (RandomForestClassifier): The trained model.
        X_new (pd.DataFrame): The new input features to predict on.

    Returns:
        predictions (np.ndarray): The predicted class labels.
    """
    predictions = model.predict(X_new)
    return predictions

def load_model(path):
    """
    Load a trained model from a file.

    Args:
        path (str): The file path to the saved model.

    Returns:
        model: The loaded model.
    """
    return joblib.load(path)
