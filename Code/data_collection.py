# Script for collecting data from Twitter API

import pandas as pd
import tweepy
from decouple import config
import time
import os


class TweetResult:
    def __init__(
        self,
        query,
        id,
        text,
        author_id,
        conversation_id,
        entities,
        geo,
        lang,
        referenced_tweets,
    ):
        self.query = query
        self.id = id
        self.text = text
        self.author_id = author_id
        self.conversation_id = conversation_id
        self.entities = entities
        self.geo = geo
        self.lang = lang
        self.referenced_tweets = referenced_tweets

    def to_dict(self):
        return {
            "query": self.query,
            "id": self.id,
            "text": self.text,
            "author_id": self.author_id,
            "conversation_id": self.conversation_id,
            "entities": self.entities,
            "geo": self.geo,
            "lang": self.lang,
            "referenced_tweets": self.referenced_tweets,
        }


# List of subjects to be used in Twitter API searches
queries = [
    "Operador Nacional do Sistema Eletrico",
    "eletricidade infraestrutura",
    "energia infraestrutura",
    "infraestrutura elétrica",
    '"geração de energia"',
    '"sistema elétrico"',
    '"energia elétrica"',
    "ONS",
]
dates = [
    ("2019-01-01T00:00:00Z", "2019-12-31T23:59:59Z"),
    ("2020-01-01T00:00:00Z", "2020-12-31T23:59:59Z"),
    ("2021-01-01T00:00:00Z", "2021-12-31T23:59:59Z"),
    ("2022-01-01T00:00:00Z", "2022-06-22T23:59:59Z"),
]

BEARER_TOKEN = config("BEARER_TOKEN")
client = tweepy.Client(BEARER_TOKEN)


def search_twitter(queries, dates):
    results = []
    for query in queries:
        for start_date, end_date in dates:
            print(start_date)
            print(end_date)
            response = client.search_all_tweets(
                query=f"{query} -is:retweet lang:pt",
                start_time=start_date,
                end_time=end_date,
                tweet_fields=[
                    "id",
                    "text",
                    "author_id",
                    "conversation_id",
                    "entities",
                    "geo",
                    "lang",
                    "referenced_tweets",
                ],
                max_results=500,
            )
            time.sleep(0.5)
            for tweet in response.data:
                result = TweetResult(
                    query,
                    tweet.id,
                    tweet.text,
                    tweet.author_id,
                    tweet.conversation_id,
                    tweet.entities,
                    tweet.geo,
                    tweet.lang,
                    tweet.referenced_tweets,
                )
                results.append(result)
    return results


def build_dataframe(tweet_results):
    return pd.DataFrame([result.to_dict() for result in tweet_results])


tweet_results = search_twitter(queries, dates)
df = build_dataframe(tweet_results)

print(df.head())
print(df.shape)

filedir = os.path.dirname(os.path.abspath(__file__))
df.to_csv(filedir + "/../Data/tweets_raw.csv")
