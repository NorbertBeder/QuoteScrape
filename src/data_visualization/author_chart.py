import matplotlib

from src.data_manipulation.count_by_option import count_by_option
import matplotlib.pyplot as plt


def author_bar_chart(csv_file):
    top_list = sorted(count_by_option(csv_file, 'author').items(), key=lambda x: x[1], reverse=True)
    top_list = top_list[:10]
    author_list = []
    quote_num = []

    for t in top_list:
        author_list.append(t[0])
        quote_num.append(t[1])

    plt.bar(author_list, quote_num, width=0.5)

    plt.title('Top 10 authors with the most quotes')

    plt.show()
