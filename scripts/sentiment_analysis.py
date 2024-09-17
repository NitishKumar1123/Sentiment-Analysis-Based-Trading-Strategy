import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon if you haven't already
nltk.download('vader_lexicon')

def perform_sentiment_analysis(df):
    sia = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['content'].apply(lambda x: sia.polarity_scores(x)['compound'])
    return df

def analyze_sentiment(input_path, output_path):
    df = pd.read_csv(input_path)
    df = perform_sentiment_analysis(df)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":

    analyze_sentiment('data/processed/financial_news_clean.csv', 'data/processed/financial_news_sentiment.csv')
    # analyze_sentiment('../data/processed/social_media_clean.csv', '../data/processed/social_media_sentiment.csv')
