# import tweepy
# import json
# import os

# # Replace these with your actual Twitter API credentials
# consumer_key = 'G6ELlRwoh35OVWHBAaxdaSc4P'
# consumer_secret = 'zxwCCJffOjFnZLtT82mw0RhnEwjYQ277zFaI4uxFKscS0x2Jz7'
# access_token = '1542424561890631680-TYJWvzjZFMMjQm90LEZC8AkAF7uQ8N'
# access_token_secret = 'RqGTYIvw1ZsJImde54gW88ggei3ftOvGAcdc6Iaf5u5Pk'
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHe%2FvwEAAAAAwp9n7rELSmlXVJMS22spqTZ5%2BOU%3DgzdBKQPrgKw5H26gatf5ef0B6rAuZcDsbi6bXxhOrs79WQBUnZ'

# # Setup Twitter API authentication
# def create_api():
#     auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
#     api = tweepy.API(auth, wait_on_rate_limit=True)
#     return api

# # Fetch tweets related to a query
# def fetch_tweets(api, query, max_tweets=100):
#     tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(max_tweets)
#     tweet_list = [{'id': tweet.id, 'created_at': tweet.created_at, 'text': tweet.full_text} for tweet in tweets]
#     return tweet_list

# # Save fetched tweets to a file
# def save_to_file(data, file_path):
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)

# if __name__ == "__main__":
#     api = create_api()
#     tweets = fetch_tweets(api, 'financial markets', max_tweets=10)
#     save_to_file(tweets, 'data/raw/social_media.json')
