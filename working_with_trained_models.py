from gensim.models import KeyedVectors


# file_name = input("Please enter vectors files:")

word_vectors = KeyedVectors.load("C:\For Talenya\Word2Vec Trial\saved_vectors1")
print(word_vectors.most_similar(positive=['king', 'woman']))
