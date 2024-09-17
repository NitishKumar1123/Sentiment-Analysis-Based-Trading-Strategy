import pandas as pd

def load_data(news_path):
    news_df = pd.read_csv(news_path)
    return news_df

def combine_features(news_df):
    # Example feature engineering - you can add more features based on your needs
    news_df['date'] = pd.to_datetime(news_df['publishedAt']).dt.date
    # For simplicity, assume we are only using sentiment scores
    features_df = news_df[['date', 'sentiment_score']]
    return features_df

def save_combined_features(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    news_df = load_data('data/processed/financial_news_sentiment.csv')
    combined_features = combine_features(news_df)
    save_combined_features(combined_features, 'data/processed/combined_features.csv')
