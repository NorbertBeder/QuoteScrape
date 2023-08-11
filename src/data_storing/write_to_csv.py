import pandas as pd


def to_csv(csv_name, object_list):
    data = []

    for obj in object_list:
        data.append(obj.__dict__)

    df = pd.DataFrame(data)
    df.to_csv(csv_name + ".csv")
