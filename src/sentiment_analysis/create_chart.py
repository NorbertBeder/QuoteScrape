from matplotlib import pyplot as plt

from src.sentiment_analysis.preprocess_text import create_sentiment_list


def sentiment_chart(table, column):
    sentiment_list = create_sentiment_list(table, column)
    negative = 0
    positive = 0
    neutral = 0

    for sentiment in sentiment_list:
        neg = sentiment['neg']
        pos = sentiment['pos']
        neu = sentiment['neu']

        if neg > pos and neg > neu:
            negative += 1
        elif pos > neg and pos > neu:
            positive += 1
        else:
            neutral += 1

    sentiments = ['positive', 'neutral', 'negative']
    scores = [positive, neutral, negative]
    print(scores)

    plt.bar(sentiments, scores, align='center', alpha=0.5)
    plt.ylabel('Count')
    plt.title('Sentiment chart')

    plt.show()

