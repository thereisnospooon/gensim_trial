import gzip
import gensim
import logging
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

hotels_data_complete = "hotels_data_concat"
hotels_data_folder = "OpinRankDatasetWithJudgments\hotels\data"
# The data for hotels in sub-folders divided by cities
card_data_folder = "OpinRankDatasetWithJudgments\cars\data"
# The data for cars in sub-folders divided by years

with open(hotels_data_complete, 'w') as data_file:
    # directory = os.fsencode("C:\For Talenya\Word2Vec Trial\OpinRankDatasetWithJudgments\hotels\data\beijing")
    for folder in os.scandir("OpinRankDatasetWithJudgments\hotels\data"):
        filename = os.fsdecode(folder)
        if filename.endswith('.csv'):
            continue
        for sub_folder in os.scandir(filename):
            try:
                with open(sub_folder, 'r') as cur_file:
                    lines = cur_file.readlines()
                    for line in lines:
                        data_file.write(line)
            except:
                continue
    # for filename in os.listdir(directory):
    #     print(filename)


