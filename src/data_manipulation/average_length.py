from src.data_reading.read_from_csv import from_csv


def calc_length(csv_file):
    quote_list = from_csv(csv_file)
    i = 0
    average = 0

    for index, row in quote_list.iterrows():
        i += 1
        average += len(row.quote)

    return average / i
