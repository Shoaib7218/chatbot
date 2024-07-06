import nltk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from training_data import training_datas
from preprocess import preprocess
from nltk.corpus import stopwords
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

# method for training set 

def prepare_training_set():
    training_set = []

    for pattern, response, category in training_datas:
        features = preprocess(pattern)
        training_set.append((features,  category))

    return training_set

def train_classifier(training_set):
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier


training_set = prepare_training_set()

classifier = train_classifier(training_set)

print(classifier.show_most_informative_features())     