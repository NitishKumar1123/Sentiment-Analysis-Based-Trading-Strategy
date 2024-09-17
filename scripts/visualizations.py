# scripts/visualizations.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_trends(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['sentiment_score'], label='Sentiment Score', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Trends')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/visualizations/sentiment_trends.png')

def plot_trading_signals(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['predicted_signal'], label='Trading Signal', color='red')
    plt.xlabel('Date')
    plt.ylabel('Signal')
    plt.title('Trading Signals')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/visualizations/trading_signals.png')

def plot_strategy_returns(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['strategy_returns'].cumsum(), label='Cumulative Strategy Returns', color='green')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.title('Strategy Returns Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/visualizations/strategy_returns.png')

if __name__ == "__main__":
    df = pd.read_csv('data/processed/backtest_results.csv')
    plot_sentiment_trends(df)
    plot_trading_signals(df)
    plot_strategy_returns(df)
