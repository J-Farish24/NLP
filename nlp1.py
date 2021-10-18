from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# print(blob.sentences)
# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)
"""
print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))

for sentence in blob.sentences:
    print(
        sentence,
        round(sentence.sentiment.polarity, 3),
        round(sentence.sentiment.subjectivity, 3),
    )
"""
"""
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)


for sentence in blob.sentences:
    print(sentence.sentiment)
"""

spanish = blob.translate(to="es")

print(spanish)

english = spanish.translate(to="en")
print(english)
