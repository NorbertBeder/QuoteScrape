from src.data_reading.read_from_csv import from_csv
from src.models.quote_model import Quotes


def filter_by_option(csv_file, option, tag):
    quote_list = from_csv(csv_file)
    option = option.lower()
    tag = tag.lower()
    filtered_list = []

    for index, row in quote_list.iterrows():
        try:
            obj_opt = row[option]
        except KeyError:
            print('Error, option not found')
            return
        if tag in obj_opt.lower():
            quote = row.quote
            author = row.author
            tags = row.tags

            filtered_list.append(Quotes(quote, author, tags))

    return filtered_list

