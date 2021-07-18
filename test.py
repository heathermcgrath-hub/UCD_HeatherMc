
import pandas as pd
import numpy as np
RPPI=pd.read_csv("Residential Property Price Index.csv")

UNEMP=pd.read_csv("Seasonally Adjusted Monthly Unemployment.csv")

UNEMPC19=pd.read_csv("Covid-19 Adjusted Monthly Unemployment Estimates.csv")

print(RPPI.info())
print(UNEMP.info())
print(UNEMPC19.info())








