import requests
import json

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '268eb2c0ae3142e8b474a553f9b4816a'
base_url = 'https://newsapi.org/v2/everything'

def fetch_financial_news(api_key, query='financial markets', page_size=100):
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': page_size
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['articles']
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return None

def save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    articles = fetch_financial_news(api_key)
    if articles:
        save_to_file(articles, 'data/raw/financial_news.json')
