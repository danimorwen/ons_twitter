# Script for collecting data from Twitter API

import pandas as pd
import tweepy
from decouple import config
import time


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
    '"geração de energia"',
    '"sistema elétrico"',
    '"energia elétrica"',
    "ONS",
]

BEARER_TOKEN = config("BEARER_TOKEN")
client = tweepy.Client(BEARER_TOKEN)


def search_twitter(queries):
    results = []
    for query in queries:
        response = client.search_all_tweets(
            query=f"{query} -is:retweet lang:pt",
            start_time="2021-07-01T00:00:00Z",
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


tweet_results = search_twitter(queries)
df = build_dataframe(tweet_results)

print(df.head())
print(df.shape)

df.to_csv("../Data/tweets_raw.csv")
