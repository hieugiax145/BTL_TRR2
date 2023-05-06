
# Import pandas
import pandas as pd
  
# reading csv file 
df = pd.read_csv('345.csv',
		header=0,
		usecols=["tip", "time"])

df
