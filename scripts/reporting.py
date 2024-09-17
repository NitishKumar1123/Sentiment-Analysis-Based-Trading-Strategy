# scripts/reporting.py
import pandas as pd

def generate_report(backtest_file, output_file):
    df = pd.read_csv(backtest_file)
    
    # Calculate total strategy return
    total_return = df['strategy_returns'].sum()
    
    # Calculate number of positive and negative signals
    positive_signals = df[df['predicted_signal'] == 1].shape[0]
    negative_signals = df[df['predicted_signal'] == 0].shape[0]
    
    with open(output_file, 'w') as f:
        f.write(f"Total Strategy Return: {total_return}\n")
        f.write(f"Number of Positive Trading Signals: {positive_signals}\n")
        f.write(f"Number of Negative Trading Signals: {negative_signals}\n")
        f.write(f"Average Daily Return: {df['strategy_returns'].mean()}\n")
        f.write(f"Total Market Returns: {df['market_returns'].sum()}\n")

if __name__ == "__main__":
    generate_report('data/processed/backtest_results.csv', 'reports/summary_report.txt')
