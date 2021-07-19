
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

#subsetting sorting and indexing RPPI data
print(RPPI_DROPDUPES.head())
print(RPPI_DROPDUPES.columns)
RPPI_DROPDUPES_FILTERED= RPPI_DROPDUPES[ (RPPI_DROPDUPES["Statistic"] == "Percentage Change over 1 month for Residential Property Price Index") & (RPPI_DROPDUPES["Type of Residential Property"] == "National - all residential properties")]
print(RPPI_DROPDUPES_FILTERED.info())
RPPI_SORTED=RPPI_DROPDUPES_FILTERED.sort_values("Month",ascending=True)
RPPI_SORTED_IND=RPPI_SORTED.set_index("Month")

#subsetting sorting and indexing UNEMP data
print(UNEMP_DROPDUPES.head())
print(UNEMP_DROPDUPES.columns)
UNEMP_DROPDUPES_FILTERED = UNEMP_DROPDUPES[(UNEMP_DROPDUPES["Statistic"] == "Seasonally Adjusted Monthly Unemployment Rate") & (UNEMP_DROPDUPES["Age Group"] == "25 - 74 years") & (UNEMP_DROPDUPES["Sex"] == "Both sexes")]
print(UNEMP_DROPDUPES_FILTERED.info())
UNEMP_SORTED = UNEMP_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
UNEMP_SORTED_IND = UNEMP_SORTED.set_index("Month")

#subsetting sorting and indexing UNEMPC19 data
print(UNEMPC19_DROPDUPES.head())
print(UNEMPC19_DROPDUPES.columns)
UNEMPC19_DROPDUPES_FILTERED = UNEMPC19_DROPDUPES[(UNEMPC19_DROPDUPES["Statistic"] == "Monthly Unemployment Rate") & (UNEMPC19_DROPDUPES["Age Group"] == "25 - 74 years") & (UNEMPC19_DROPDUPES["Sex"] == "Both sexes") & (UNEMPC19_DROPDUPES["Lower and Upper Bound"] == "Upper Bound (COVID-19 Adjusted MUR)")]
print(UNEMPC19_DROPDUPES_FILTERED.info())
UNEMPC19_SORTED = UNEMPC19_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
UNEMPC19_SORTED_IND = UNEMPC19_SORTED.set_index("Month")

#merge UNEMP and UNEMPC19 data
print(UNEMP_SORTED_IND.shape)
UNEMP_MERGE = UNEMP_SORTED_IND.merge(UNEMPC19_SORTED_IND, on="Month", how="outer")
print(UNEMP_MERGE.shape)
print(UNEMP_MERGE.columns)

#merge UNEMP and RPPI data

UNEMP_RPPI_MERGE = UNEMP_MERGE.merge(RPPI_SORTED_IND, on="Month", how="outer")
print(UNEMP_RPPI_MERGE.shape)
print(UNEMP_RPPI_MERGE.columns)

#removing unwanted dates and columns
UNEMP_RPPI_MERGE_CLEAN = UNEMP_RPPI_MERGE.loc["2015":"2022"]
print(UNEMP_RPPI_MERGE_CLEAN.shape)
UNEMP_RPPI_MERGE_CLEAN2 = UNEMP_RPPI_MERGE_CLEAN.drop(columns = ['Age Group_x','Sex_x','UNIT_x','Statistic_y', 'Age Group_y', 'Sex_y','UNIT_y','UNIT'])
print(UNEMP_RPPI_MERGE_CLEAN2.shape)
print(UNEMP_RPPI_MERGE_CLEAN2.columns)
print(UNEMP_RPPI_MERGE_CLEAN2.head())






