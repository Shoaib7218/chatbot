import nltk # natural language toolkit
from nltk.tokenize import word_tokenize # to sslpit the sentence into words
from nltk.corpus import stopwords # to remove stopwords for eg like ,and, is

nltk.download('punkt') #package used for tokenizing sentence into words
nltk.download('stopwords') #package used for removing stopwords

stop_words = set(stopwords.words('english'))  # taking stopwords from the package for language english


def preprocess(sentence):

    words = word_tokenize(sentence.lower()) # making words from sentences
    words = [word for word in words if word.isalnum and word not in stop_words] # removing words which are in stop words and alphanumric nos

    features = {}
    for word in words:
        features[word] = True 
    if '?' in sentence:
        features['questions'] = True
    else:
        features['statement'] = True
    return features


test_sen = "courses"

print(preprocess(test_sen))

