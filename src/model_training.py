import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data(file_path):
    """Load processed data."""
    return pd.read_csv(file_path)

def train_model(X, y):
    """Train a RandomForest model."""
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

if __name__ == "__main__":
    # Update the file path to the processed data
    data = load_data('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/processed/processed_data_with_features.csv')
    
    # Update column names according to your dataset
    X = data[['Temperature_Mean', 'Vibration_Mean', 'Pressure_Mean', 'RPM_Mean']]
    y = data['Maintenance Required']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, 'C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/models/random_forest_model.pkl')