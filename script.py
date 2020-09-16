from io import TextIOWrapper
from datetime import datetime

class DataAnalysis:

  def __init__(self):
    self.csv_data=[]
    self.processed_data=[]

  def read_csv(self,filename):
      import csv
      with open(filename, 'rt', encoding='utf8') as f:
        self.csv_data = list(csv.DictReader(f))
      for index,row in enumerate(self.csv_data):
        date=row['Date']
        death_rate=row['Deaths per 1000 People']
        annual_change=row['Annual % Change']
        self.processed_data.append((datetime.strptime(date, '%m/%d/%Y'), death_rate, annual_change))
        print(index, row['Date'], row['Deaths per 1000 People'], row['Annual % Change'])

    
if __name__ == '__main__':
  data_analysis = DataAnalysis()
  data_analysis.read_csv('./india_death_rate.csv')