import pandas as pd
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def load_model(file_path):
    return joblib.load(file_path)

def simulate_market_returns(df):
    # Simulate market returns if not available
    if 'market_returns' not in df.columns:
        df['market_returns'] = 0.01  # Example: constant return for simplicity
    return df

def backtest_strategy(df, model):
    # Simulate market returns if they are not present
    df = simulate_market_returns(df)
    
    X = df[['sentiment_score']]
    df['predicted_signal'] = model.predict(X)
    
    # Calculate strategy returns
    df['strategy_returns'] = df['predicted_signal'] * df['market_returns']
    
    total_return = df['strategy_returns'].sum()
    print(f'Total Strategy Return: {total_return:.2f}')
    
    # Optionally, return dataframe for further inspection
    return df

if __name__ == "__main__":
    df = load_data('data/processed/combined_features.csv')
    model = load_model('models/trained_model.pkl')
    result_df = backtest_strategy(df, model)
    # Optionally save the result dataframe
    result_df.to_csv('data/processed/backtest_results.csv', index=False)
