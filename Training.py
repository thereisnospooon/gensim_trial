import gensim
import logging
from gensim.models import KeyedVectors

input_file = input("Please enter file to learn")
saved_file = input("Please enter path of file to save vectors to:")


def read_input(input_file):
    """This method reads the input file """

    logging.info("reading file {0}...this may take a while".format(input_file))

    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i % 10000 == 0:
                logging.info("read {0} reviews".format(i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess(line)


documents = list(read_input(input_file))
logging.info("Done reading data file")
model = gensim.models.Word2Vec(documents, size=150, window=10, min_count=2, workers=10)
model.train(documents, total_examples=len(documents), epochs=10)
word_vectors = model.wv
word_vectors.save(saved_file)
word_vectors = KeyedVectors.load(saved_file)

