from nltk.stem import SnowballStemmer
from nltk import pos_tag, word_tokenize

def snowball_stemming_pos_tag(text):
    stemmer = SnowballStemmer("english")
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    tagged_tokens = pos_tag(stemmed_tokens)
    return tagged_tokens

# Example usage:
text = "The quick brown foxes are jumping over the lazy dogs"
tagged_tokens = snowball_stemming_pos_tag(text)
print(tagged_tokens)