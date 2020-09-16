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

  def get_death_rate(self, from_year, to_year):
    total_death = 0
    num_of_years = to_year - from_year + 1

    for item in self.processed_data:
      date = item[0]
      year = date.year
      death_rate = item[1]

      print(year)
      if year >= from_year and year <= to_year:
        total_death += float(death_rate)

    total_death_rate = total_death/num_of_years

    print(f'Total death rate between years {from_year} and {to_year} (Including both) is: {total_death_rate}')

    
if __name__ == '__main__':
  data_analysis = DataAnalysis()
  data_analysis.read_csv('./india_death_rate.csv')
  data_analysis.get_death_rate(1960, 2017)