
import pandas as pd
import numpy as np
RPPI=pd.read_csv("Residential Property Price Index.csv")
UNEMP=pd.read_csv("Seasonally Adjusted Monthly Unemployment.csv")
UNEMPC19=pd.read_csv("Covid-19 Adjusted Monthly Unemployment Estimates.csv")

print(RPPI.info())
print(UNEMP.info())
print(UNEMPC19.info())

print(RPPI.shape)
print(UNEMP.shape)
print(UNEMPC19.shape)

print(RPPI.head())
print(UNEMP.head())
print(UNEMPC19.head())

#bfill and ffill data

NEW_RPPI_FILLED=RPPI.fillna(method="bfill").fillna(method="ffill")
NEW_UNEMP_FILLED=UNEMP.fillna(method="bfill").fillna(method="ffill")
NEW_UNEMPC19_FILLED=UNEMPC19.fillna(method="bfill").fillna(method="ffill")

print(NEW_RPPI_FILLED.info())
print(NEW_UNEMP_FILLED.info())
print(NEW_UNEMPC19_FILLED.info())

#drop duplictes
RPPI_DROPDUPES=NEW_RPPI_FILLED.drop_duplicates()
UNEMP_DROPDUPES=NEW_UNEMP_FILLED.drop_duplicates()
UNEMPC19_DROPDUPES=NEW_UNEMPC19_FILLED.drop_duplicates()

print(RPPI_DROPDUPES.info())
print(UNEMP_DROPDUPES.info())
print(UNEMPC19_DROPDUPES.info())










