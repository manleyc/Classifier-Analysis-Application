from sklearn.model_selection import train_test_split
import pandas as pd

def addHeaders(csv_file):

    colNum = len(csv_file.columns)

    colHeaders = []
    for i in range(colNum):
        colHeaders.append('column ' + str(i+1))

    csv_file.columns = colHeaders
    return csv_file




      

