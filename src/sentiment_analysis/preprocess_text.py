from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from src.sentiment_analysis.read_mysql import read_from_mysql


def preprocess(table, column):
    data_list = read_from_mysql(table, column)
    lemmatizer = WordNetLemmatizer()

    processed_sentence = []

    for data in data_list:
        sentence = word_tokenize(data[0])
        filtered_sentence = [stop for stop in sentence if not stop.lower() in stopwords.words('english')]

        lemmatized_sentence = [lemmatizer.lemmatize(lem) for lem in filtered_sentence]
        processed_sentence.append(' '.join(lemmatized_sentence))

    return processed_sentence


def create_sentiment_list(table, column):
    analyzer = SentimentIntensityAnalyzer()

    sentiment_list = []

    processed_sentences = preprocess(table, column)
    for sentence in processed_sentences:
        sentiment_list.append(analyzer.polarity_scores(sentence))

    return sentiment_list
