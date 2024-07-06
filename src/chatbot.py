# chatbot.py

import sys
import os
sys.path.append(os.path.abspath(''))

import nltk
from src.preprocess import preprocess
from src.train import train_classifier
from training_data import training_datas  # Import training data directly

def classify_input(input_text, classifier):
    featureset = preprocess(input_text)
    return classifier.classify(featureset)

def get_response(input_text, classifier):
    category = classify_input(input_text, classifier)
    for pattern, response, cat in training_datas:
        if pattern.lower() == input_text.lower():
            return response
        # if user_input.lower() == "stop":
        #     return "Bye! See you again soon."
    return "Sorry, I don't understand that."

def load_classifier():
    training_set = [(preprocess(pattern), category) for pattern, response, category in training_datas]
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier

if __name__ == "__main__":
    classifier = load_classifier()

    # user_input = ""
    # while user_input != "stop":
    #     user_input = input()
    #     response = get_response(user_input, classifier)
    #     print(f"User: {user_input}")
    #     print(f"Bot: {response}")
        
    
