import pandas as pd

def load_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        data_df = pd.read_csv(file)
        return data_df

teams_df = load_csv('./nbaData/teams.csv')


# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()