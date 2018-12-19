from gensim.models import KeyedVectors


# file_name = input("Please enter vectors files:")

word_vectors = KeyedVectors.load("vectors.vec")
print(word_vectors.most_similar(positive=['king']))
