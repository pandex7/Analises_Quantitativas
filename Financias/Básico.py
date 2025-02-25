import numpy
import pandas
import matplotlib
import math
import random
import statsmodels
import pandas_datareader

introdução 

#ARRAYS
import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
a
a.shape
a[1,3]
a[1,2] = 8

a[0]
a[1]

#random
import random
prob = random.random()
print (prob)
number = random.randint(1,6)
print(number)
import numpy as np
np.random.randint(1,6,(4,6))

#Organizing
import numpy as np
import pandas as pd

ser = pd.Series(np.random.random(5), name = "Coluna 01")
ser
ser[3]
from pandas_datareader import data as wb
PG = wb.DataReader("PG", data_source="yahoo", start="1995-1-1")
PG
PG.info() #Informação dos dados
PG.head() #Primeiras 5 linhas
PG.tail() #Ultimas 5 linhas
#Se quiser olhar um certo numero de linhas especificar (20) e etc.. exemplo >
PG.head(20)
PG.tail(20) 

tickers = ["PG", "MSFT", "T", "F", "GE"]
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source="yahoo", start="1995-1-1")["Adj Close"]
    new_data.tail()
#para subtituir o web e so trocar o yahoo por morningstar ou iex

import quandl
mydata_01 = quandl.get ("FRED/GDP")
mydata_01.tail()
mydata_01.head()

import pandas as pd
mydata_01.to_csv("C:/Users/Cliente/Desktop/Python/Careers/Aula 1/example_01.csv") #vscode para o pc
mydata_02 = pd.read_csv("C:/Users/Cliente/Desktop/Python/Careers/Aula 1/Data_02.csv")#pc para o vscode
mydata_02.head()
mydata_02.tail()
mydata_02.to_excel("C:/Users/Cliente/Desktop/Python/Careers/Aula 1/example_02.xlsx")
mydata_03 = pd.read_excel("C:/Users/Cliente/Desktop/Python/Careers/Aula 1/Data_03.xlsx")
mydata_03
mydata_02 = pd.read_csv("C:/Users/Cliente/Desktop/Python/Careers/Aula 1/Data_02.csv", index_col="Date")
mydata_02
mydata_03
mydata_03.set_index("Year")
mydata_03 = mydata_03.set_index("Year")
mydata_03 
