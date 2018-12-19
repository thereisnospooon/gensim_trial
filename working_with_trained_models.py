from gensim.models import KeyedVectors


# file_name = input("Please enter vectors files:")

word_vectors = KeyedVectors.load("saved_vectors.vec")
print(word_vectors.most_similar(positive=['king', 'woman']))
