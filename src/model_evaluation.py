import pandas as pd
from sklearn.metrics import classification_report
import joblib
from sklearn.model_selection import train_test_split

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return report

if __name__ == "__main__":
    # Update the file path to load the model
    model = joblib.load('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/models/random_forest_model.pkl')
    
    # Update the file path to load the processed data
    data = pd.read_csv('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/processed/processed_data_with_features.csv')
    
    # Update column names according to your dataset
    X = data[['Temperature_Mean', 'Vibration_Mean', 'Pressure_Mean', 'RPM_Mean']]
    y = data['Maintenance Required']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Evaluate the model
    report = evaluate_model(model, X_test, y_test)
    print(report)
