import csv
import numpy as np

def getDataSouce(data_path):
    size_of_tv = []
    average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spent.apend(float(row['\t Average time spent watching TV in a week (hours)']))

    return{'x': size_of_tv , 'y':average_time_spent}  

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between size of tv and average time spent watching tv in a week \n ',correlation[0,1])

def setup():
    data_path = 'Size of TV,_Average time spent watching TV in a week (hours).csv'

    dataSource = getDataSouce(data_path)
    findCorrelation(dataSource)

setup()
    