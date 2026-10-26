import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as NLTKVADER
from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer as StandaloneVADER
)

# Download VADER lexicon for NLTK
nltk.download("vader_lexicon", quiet=True)

df = pd.read_csv("product_reviews.csv")
df["Review"] = df["Review"].fillna("").astype(str)

# Initialize both implementations
nltk_analyzer = NLTKVADER()
vader_analyzer = StandaloneVADER()

def classify(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"

# NLTK VADER scores
nltk_scores = df["Review"].apply(
    nltk_analyzer.polarity_scores
)

df["nltk_positive"] = nltk_scores.apply(lambda x: x["pos"])
df["nltk_negative"] = nltk_scores.apply(lambda x: x["neg"])
df["nltk_neutral"] = nltk_scores.apply(lambda x: x["neu"])
df["nltk_compound"] = nltk_scores.apply(lambda x: x["compound"])

# Standalone VADER scores
vader_scores = df["Review"].apply(
    vader_analyzer.polarity_scores
)

df["vader_positive"] = vader_scores.apply(lambda x: x["pos"])
df["vader_negative"] = vader_scores.apply(lambda x: x["neg"])
df["vader_neutral"] = vader_scores.apply(lambda x: x["neu"])
df["vader_compound"] = vader_scores.apply(lambda x: x["compound"])

df["nltk_sentiment"] = df["nltk_compound"].apply(classify)
df["vader_sentiment"] = df["vader_compound"].apply(classify)

# Display sample results
print(df[[
    "Review",
    "nltk_compound",
    "nltk_sentiment",
    "vader_compound",
    "vader_sentiment"
]].head(10).to_string(index=False))

# Count sentiment categories
print("\nNLTK sentiment distribution:")
print(df["nltk_sentiment"].value_counts())

print("\nStandalone VADER sentiment distribution:")
print(df["vader_sentiment"].value_counts())

# Save output
df.to_csv("sentiment_analysis_results.csv", index=False)
print("\nResults saved to sentiment_analysis_results.csv")