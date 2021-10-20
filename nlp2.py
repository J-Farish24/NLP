from textblob import TextBlob
import nltk

from pathlib import Path
import pandas as pd

'nltk.download("stopwords")'
from nltk.corpus import stopwords

stops = stopwords.words("english")
"""
"print(stops)"

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]
"""
"print(cleanlist)"

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.words.count("joy"))

print(blob.word_counts["juliet"])

more_stops = ["thee", "thy", "thou"]

stops += more_stops

items = blob.word_counts.items()

clean_items = [item for item in items if item[0] not in stops]

from operator import itemgetter

sorted_items = sorted(clean_items, key=itemgetter(1), reverse=True)

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=["word", "count"])

print(df)
input()

import matplotlib.pyplot as plt

df.plot.bar(x="word", y="count", legend=False, color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout()

plt.show()
