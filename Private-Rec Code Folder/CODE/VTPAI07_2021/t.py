import pandas as pd
from textblob import TextBlob

def reviewCount(name):
    df = pd.read_csv('review.csv')
    df = df[df['name'].str.contains(name)]
    d = df['reviews.title']
    t = 0 
    p = 0
    n = 0
    nu = 0
    for x in d:
        t += 1
        analysis = TextBlob(x)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            p += 1
        elif sentiment < 0:
            n += 1
        else:
            nu += 1
    l = [p, n, nu, t]
    return l

