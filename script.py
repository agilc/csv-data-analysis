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
        # print(index, row['Date'], row['Deaths per 1000 People'], row['Annual % Change'])

  def get_death_rate(self, from_year, to_year):
    total_death = 0
    num_of_years = to_year - from_year + 1

    for item in self.processed_data:
      date = item[0]
      year = date.year
      death_rate = item[1]

      if year >= from_year and year <= to_year:
        total_death += float(death_rate)

    total_death_rate = total_death/num_of_years

    print(f'Total death rate between years {from_year} and {to_year} (Including both) is: {total_death_rate}')


  def get_average_median_variance(self, from_year, to_year):
    death_rate_list = []
    total_death = 0
    num_of_years = to_year - from_year + 1

    for item in self.processed_data:
      date = item[0]
      year = date.year
      death_rate = item[1]

      if year >= from_year and year <= to_year:
        total_death += float(death_rate)
        death_rate_list.append(death_rate)

    average_death_rate = total_death/num_of_years
    death_rate_list.sort()

  
    median = 0
    if(num_of_years%2==0):
      mid = num_of_years//2
      median = (float(death_rate_list[mid-1]) + float(death_rate_list[mid]))/2
    else:
      mid = num_of_years//2
      median = death_rate_list[mid]

    variance = 0
    for item in death_rate_list:
      variance += pow(average_death_rate-float(item), 2)

    variance = variance/len(death_rate_list)


    print(f'From {from_year} and {to_year}, average death rate = {average_death_rate}, median={median}, Variance={variance}')
    
if __name__ == '__main__':
  data_analysis = DataAnalysis()
  data_analysis.read_csv('./india_death_rate.csv')
  print('----------------Question 1:--------------------')
  data_analysis.get_death_rate(1960, 2017)
  print('----------------Question 3:--------------------')
  data_analysis.get_average_median_variance(1960,1969)
  data_analysis.get_average_median_variance(1970,1979)
  data_analysis.get_average_median_variance(1980,1989)
  data_analysis.get_average_median_variance(1990,1999)
  data_analysis.get_average_median_variance(2000,2009)
  data_analysis.get_average_median_variance(2010,2017)


#   Use Python, R, or less preferably Excel to answer the following questions. If you use R or Python, send the scripts as well. If you use Excel, please make sure you keep the formulas in the sheet.
# * Plot the death rate of India between 1960 and 2017
#     * What period saw India’s death rate falling fastest? What happened then to cause the change?
# * Calculate the average, median, and variance of India’s death rate in the periods of 1960-1969, 1970-1979, 1980-1989, 1990-1999, 2000-2009, and 2010-2017 respectively

# (Note: The evaluation of this question is based on the progress but not necessarily the result. If you couldn’t get to the final answer, reply with the best progress you’ve made)