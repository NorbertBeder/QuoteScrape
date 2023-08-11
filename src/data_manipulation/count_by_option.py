from src.data_reading.read_from_csv import from_csv


def count_by_option(csv_file, option):
    quote_list = from_csv(csv_file)
    quote_num = {}

    for index, row in quote_list.iterrows():
        try:
            obj_opt = row[option]
        except KeyError:
            print('Error, option not found')
            return
        if obj_opt not in quote_num:
            quote_num[obj_opt] = 1
        else:
            quote_num[obj_opt] += 1

    return quote_num
