import pandas as pd
import json
import re

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text.lower()

def preprocess_financial_news(input_path, output_path):
    articles = load_json(input_path)
    df = pd.DataFrame(articles)
    df['description'] = df['description'].apply(preprocess_text)
    df.to_csv(output_path, index=False)

def preprocess_social_media(input_path, output_path):
    tweets = load_json(input_path)
    df = pd.DataFrame(tweets)
    df['text'] = df['text'].apply(preprocess_text)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_financial_news('data/raw/financial_news.json', 'data/processed/financial_news_clean.csv')
    # preprocess_social_media('../data/raw/social_media.json', '../data/processed/social_media_clean.csv')

