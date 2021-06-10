# Natural Language 2020/2021, Mini-Project 1
# Joao Parreiro, 89483 / Joao Vieira, 90739

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import sys

nltk.download("punkt")


def preprocessing(question):
    ps = PorterStemmer()

    question = re.sub(r"``(.+?)\'\'", "QUOTED_EXPRESSION", question)
    processed_question = ""
    for word in word_tokenize(question):
        word = ps.stem(word)
        processed_question = processed_question + " " + word

    return processed_question


# Read command line arguments
if len(sys.argv) != 4:
    print("ERROR: Invalid number of arguments!")
    sys.exit(1)

label_type = sys.argv[1]
train_file = open(sys.argv[2])
test_questions_file = open(sys.argv[3])

# Get labels and questions
train_fine_labels = []
train_questions = []
for line in train_file:
    substrings = re.split(" ", line, 1)
    train_fine_labels.append(substrings[0])
    train_questions.append(preprocessing(substrings[1]))

train_coarse_labels = []
for label in train_fine_labels:
    substrings = re.split(":", label, 1)
    train_coarse_labels.append(substrings[0])

test_questions = []
for line in test_questions_file:
    test_questions.append(preprocessing(line))

train_file.close()
test_questions_file.close()

# Train and test
count_vectorizer = CountVectorizer(ngram_range=(1, 3))

train_questions_count = count_vectorizer.fit_transform(train_questions)
test_questions_count = count_vectorizer.transform(test_questions)

cos_sim = cosine_similarity(train_questions_count, test_questions_count)
cos_sim = cos_sim.transpose()
if label_type == "-coarse":
    for entry in cos_sim:
        min_index = np.argmax(entry)
        print(train_coarse_labels[min_index])
elif label_type == "-fine":
    for entry in cos_sim:
        min_index = np.argmax(entry)
        print(train_fine_labels[min_index])
else:
    print("ERROR: Invalid label type!")
    sys.exit(1)
