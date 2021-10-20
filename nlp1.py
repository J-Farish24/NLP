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
"""
spanish = blob.translate(to="es")
chinese = blob.translate(to="zh")


print(spanish)
print(chinese)

english = spanish.translate(to="en")
print(english)
"""

from textblob import Word

"""
index = Word("index")
print(index.pluralize())

cacti = Word("catci")
print(cacti.singularize())

animals = TextBlob("Cat Dog Fish Bird").words

print(animals.pluralize())


word = Word("theyr")
print(word.spellcheck())
print(word.correct())"""
"""
word1 = Word("studies")
word2 = Word("varieties")

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())
"""
happy = Word("happy")

print(happy.definitions)

print(happy.synsets)

for s in happy.synsets:
    for lemma in s.lemmas():
        print(lemma.name())

synoynm = happy.synsets[1].lemmas()[0].name()
print(synoynm)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)
