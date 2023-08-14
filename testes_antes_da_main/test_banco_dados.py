import csv
import pandas as pd

def main():
    file_name = 'ar_condicionado.csv'
    header = ('Rank', 'Raiting','Title')
    data = [(1, 9.2, "The Shawshank Redemption(1994)"),
            (2, 9.2, "The Godfather(1972)"),
            (3, 9, "The Godfather: Part II(1974)"),
            (4, 8.9, "Pulp Fiction(1994)")
    ]
    writer(header, data, file_name, 'write')
    updater(file_name)

def writer(header, data, file_name, option):
     with open (file_name, "w", newline = "") as csvfile:
        if option == 'write':

            movies = csv.writer(csvfile)
            movies.writerow(header)
            for x in data:
                movies.writerow(x)
        elif option =='update':
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")

''''''
def updater(file_name):
    with open(file_name, newline= "") as file:
        read_data = [row for row in csv.DictReader(file)]
        read_data[0]['Raiting'] = '9.9999'

    readHeader = read_data[0].keys()
    writer(readHeader, read_data, file_name, 'update')


