import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def create_target_variable(df):
    # Define target variable, e.g., binary classification based on sentiment score
    df['target'] = df['sentiment_score'].apply(lambda x: 1 if x > 0 else 0)  # Example: positive sentiment = 1, else = 0
    return df

def train_model(df):
    df = create_target_variable(df)
    X = df[['sentiment_score']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')
    
    return model

def save_model(model, file_path):
    joblib.dump(model, file_path)

if __name__ == "__main__":
    df = load_data('data/processed/combined_features.csv')
    model = train_model(df)
    save_model(model, 'models/trained_model.pkl')
