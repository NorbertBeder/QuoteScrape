from dotenv import load_dotenv

from src.data_extractors.extract import get_quotes
from src.data_manipulation.average_length import calc_length
from src.data_manipulation.count_by_option import count_by_option
from src.data_manipulation.filter_by_option import filter_by_option
from src.data_storing.write_to_csv import to_csv
from src.data_visualization.author_chart import author_bar_chart
from src.db.populate import write_to_mariadb
from src.sentiment_analysis.create_chart import sentiment_chart
from src.sentiment_analysis.read_mysql import read_from_mysql

if __name__ == '__main__':
    load_dotenv()
        #get objects and save to database and csv
    object_list = get_quotes()
    write_to_mariadb(object_list)
    to_csv('quotes', object_list)

    print(count_by_option('quotes', 'author'))

        #Filter by option and tag
    filtered_list = filter_by_option('quotes', 'tags', 'inspirational')
    to_csv('filtered', filtered_list)
    print(calc_length('quotes'))
    author_bar_chart('quotes')
    read_from_mysql('quote', 'text')
    sentiment_chart('quote', 'text')
