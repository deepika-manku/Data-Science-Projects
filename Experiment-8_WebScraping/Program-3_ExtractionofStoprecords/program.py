import re
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from collections import Counter
nltk.download("stopwords", quiet=True)
df = pd.read_csv("product_reviews.csv")
df["Review"] = df["Review"].fillna("").astype(str)
stop_words = set(stopwords.words("english"))
def analyze_review(text):
    tokens = re.findall(r"\b[\w']+\b", text.lower())
    words = re.findall(r"\b[A-Za-z]+\b", text)
    numeric_tokens = re.findall(r"\b\d+(?:\.\d+)?\b", text)
    stopword_tokens = [
        token for token in tokens if token in stop_words
    ]
    return pd.Series({
        "word_count": len(tokens),
        "character_count": len(text),
        "numeric_count": len(numeric_tokens),
        "stopword_count": len(stopword_tokens),
        "average_word_length": (
            sum(len(word) for word in words) / len(words)
            if words else 0
        )
    })
statistics = df["Review"].apply(analyze_review)
df = pd.concat([df, statistics], axis=1)
df.to_csv("review_statistics.csv", index=False)
columns = [
    ("stopword_count", "Stopword Count"),
    ("numeric_count", "Numeric Token Count"),
    ("word_count", "Word Count"),
    ("character_count", "Character Count"),
    ("average_word_length", "Average Word Length")
]
fig, axes = plt.subplots(3, 2, figsize=(14, 15))
axes = axes.flatten()
for i, (column, title) in enumerate(columns):
    sns.histplot(
        data=df, x=column, kde=True,
        ax=axes[i], bins=20
    )
    axes[i].set_title(title)
    axes[i].set_xlabel(title)
    axes[i].set_ylabel("Number of Reviews")
axes[-1].axis("off")
plt.tight_layout()
plt.savefig("review_statistics_distributions.png", dpi=300)
plt.show()
all_tokens = re.findall(
    r"\b[\w']+\b",
    " ".join(df["Review"]).lower()
)
stopword_frequency = Counter(
    token for token in all_tokens if token in stop_words
)
print("Top 10 stopwords:")
print(stopword_frequency.most_common(10))
print("\nDescriptive statistics:")
print(df[[
    "stopword_count",
    "numeric_count",
    "word_count",
    "character_count",
    "average_word_length"
]].describe())