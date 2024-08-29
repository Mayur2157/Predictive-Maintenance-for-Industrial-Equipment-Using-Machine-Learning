import pandas as pd

def create_features(df):
    """Generate additional features from raw data."""
    df['Temperature_Mean'] = df['Temperature (°C)'].rolling(window=5).mean()
    df['Vibration_Mean'] = df['Vibration (mm/s)'].rolling(window=5).mean()
    df['Pressure_Mean'] = df['Pressure (Pa)'].rolling(window=5).mean()
    df['RPM_Mean'] = df['RPM'].rolling(window=5).mean()
    return df

if __name__ == "__main__":
    # Update the file path according to your file location
    data = pd.read_csv('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/processed/processed_data.csv')
    
    # Generate additional features
    data = create_features(data)
    
    # Save the updated data
    data.to_csv('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/data/processed/processed_data_with_features.csv', index=False)
