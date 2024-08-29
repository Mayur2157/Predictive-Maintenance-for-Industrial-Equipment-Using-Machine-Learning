import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and outliers."""
    df = df.dropna()
    # Handling outliers can be added here
    return df

def scale_features(df, features):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df

def preprocess_data(df):
    if df.empty:
        return df

    # Preprocessing logic: calculate changes in temperature and vibration
    df['Temp_Change'] = df['Temperature (°C)'].diff()
    df['Vib_Change'] = df['Vibration (mm/s)'].diff()

    # Handle NaN values resulting from .diff()
    df.fillna(0, inplace=True)
    
    return df



if __name__ == "__main__":
    # Update the path according to your file location
    data = load_data('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/raw/equipment_data.csv')
    
    # Clean the dataset
    data = clean_data(data)
    
    # Define the features to scale
    features_to_scale = [
        'Temperature (°C)', 'Vibration (mm/s)', 'Pressure (Pa)', 'RPM', 
        'Temp_Change', 'Vib_Change'
    ]
    
    # Scale the features
    data = scale_features(data, features_to_scale)
    
    # Save the processed data
    data.to_csv('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/processed/processed_data.csv', index=False)
