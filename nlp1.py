from nltk.stem import SnowballStemmer

# Initialize Snowball stemmer for English
stemmer = SnowballStemmer('english')

# Example words
words = ["running", "easily", "friendship", "prettiness", "quickly", "beautifully"]

# Stem each word
stemmed_words = [stemmer.stem(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)