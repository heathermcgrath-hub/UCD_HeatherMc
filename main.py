
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

RPPI = pd.read_csv("Residential Property Price Index.csv")
RPPI2 = pd.read_csv("RPPI2.csv")
UNEMP = pd.read_csv("Seasonally Adjusted Monthly Unemployment.csv")
UNEMPC19 = pd.read_csv("Covid-19 Adjusted Monthly Unemployment Estimates.csv")

print(RPPI.info())
print(RPPI2.info())
print(UNEMP.info())
print(UNEMPC19.info())

print(RPPI.shape)
print(RPPI2.shape)
print(UNEMP.shape)
print(UNEMPC19.shape)

print(RPPI.head())
print(RPPI2.head())
print(UNEMP.head())
print(UNEMPC19.head())

# bfill and ffill data

NEW_RPPI_FILLED = RPPI.fillna(method="bfill").fillna(method="ffill")
NEW_RPPI2_FILLED = RPPI.fillna(method="bfill").fillna(method="ffill")
NEW_UNEMP_FILLED = UNEMP.fillna(method="bfill").fillna(method="ffill")
NEW_UNEMPC19_FILLED = UNEMPC19.fillna(method="bfill").fillna(method="ffill")

print(NEW_RPPI_FILLED.info())
print(NEW_RPPI2_FILLED.info())
print(NEW_UNEMP_FILLED.info())
print(NEW_UNEMPC19_FILLED.info())

# drop duplicates
RPPI_DROPDUPES = NEW_RPPI_FILLED.drop_duplicates()
RPPI2_DROPDUPES = NEW_RPPI2_FILLED.drop_duplicates()
UNEMP_DROPDUPES = NEW_UNEMP_FILLED.drop_duplicates()
UNEMPC19_DROPDUPES = NEW_UNEMPC19_FILLED.drop_duplicates()

print(RPPI_DROPDUPES.info())
print(RPPI2_DROPDUPES.info())
print(UNEMP_DROPDUPES.info())
print(UNEMPC19_DROPDUPES.info())

# subsetting sorting and indexing RPPI data
print(RPPI_DROPDUPES.head())
print(RPPI_DROPDUPES.columns)
RPPI_DROPDUPES_FILTERED = RPPI_DROPDUPES[(RPPI_DROPDUPES["Statistic"] ==
                                          "Percentage Change over 1 month for Residential Property Price Index")
                                         & (RPPI_DROPDUPES["Type of Residential Property"] ==
                                            "National - all residential properties")]
print(RPPI_DROPDUPES_FILTERED.info())
RPPI_SORTED = RPPI_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
RPPI_SORTED_IND = RPPI_SORTED.set_index("Month")

# subsetting sorting and indexing RPPI2 data
print(RPPI2_DROPDUPES.head())
print(RPPI2_DROPDUPES.columns)
RPPI2_DROPDUPES_FILTERED = RPPI2_DROPDUPES[(RPPI2_DROPDUPES["Statistic"] == "Residential Property Price Index")
                                           & (RPPI2_DROPDUPES["Type of Residential Property"] ==
                                              "National - all residential properties")]
print(RPPI2_DROPDUPES_FILTERED.info())
RPPI2_SORTED = RPPI2_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
RPPI2_SORTED_IND = RPPI2_SORTED.set_index("Month")
RPPI2_SORTED_IND.columns = ['Statistic2', 'Type of Residential Property2', 'UNIT2', 'VALUE2']
print(RPPI2_SORTED_IND.columns)
print(RPPI2_SORTED_IND.head())

# subsetting sorting and indexing UNEMP data
print(UNEMP_DROPDUPES.head())
print(UNEMP_DROPDUPES.columns)
UNEMP_DROPDUPES_FILTERED = UNEMP_DROPDUPES[(UNEMP_DROPDUPES["Statistic"] ==
                                            "Seasonally Adjusted Monthly Unemployment Rate")
                                           & (UNEMP_DROPDUPES["Age Group"] == "25 - 74 years")
                                           & (UNEMP_DROPDUPES["Sex"] == "Both sexes")]
print(UNEMP_DROPDUPES_FILTERED.info())
UNEMP_SORTED = UNEMP_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
UNEMP_SORTED_IND = UNEMP_SORTED.set_index("Month")

# subsetting sorting and indexing UNEMPC19 data
print(UNEMPC19_DROPDUPES.head())
print(UNEMPC19_DROPDUPES.columns)
UNEMPC19_DROPDUPES_FILTERED = UNEMPC19_DROPDUPES[(UNEMPC19_DROPDUPES["Statistic"] ==
                                                  "Monthly Unemployment Rate")
                                                 & (UNEMPC19_DROPDUPES["Age Group"] == "25 - 74 years")
                                                 & (UNEMPC19_DROPDUPES["Sex"] == "Both sexes")
                                                 & (UNEMPC19_DROPDUPES["Lower and Upper Bound"] ==
                                                    "Upper Bound (COVID-19 Adjusted MUR)")]
print(UNEMPC19_DROPDUPES_FILTERED.info())
UNEMPC19_SORTED = UNEMPC19_DROPDUPES_FILTERED.sort_values("Month", ascending=True)
UNEMPC19_SORTED_IND = UNEMPC19_SORTED.set_index("Month")

# merge UNEMP and UNEMPC19 data
print(UNEMP_SORTED_IND.shape)
UNEMP_MERGE = UNEMP_SORTED_IND.merge(UNEMPC19_SORTED_IND, on="Month", how="outer")
print(UNEMP_MERGE.shape)
print(UNEMP_MERGE.columns)

# merge UNEMP and RPPI data

UNEMP_RPPI_MERGE1 = UNEMP_MERGE.merge(RPPI_SORTED_IND, on="Month", how="outer")
UNEMP_RPPI_MERGE = UNEMP_RPPI_MERGE1.merge(RPPI2_SORTED_IND, on="Month", how="outer")
print(UNEMP_RPPI_MERGE.shape)
print(UNEMP_RPPI_MERGE.columns)

# removing unwanted dates and columns
UNEMP_RPPI_MERGE_CLEAN = UNEMP_RPPI_MERGE.loc["2015":"2022"]
print(UNEMP_RPPI_MERGE_CLEAN.shape)
print(UNEMP_RPPI_MERGE_CLEAN.columns)
UNEMP_RPPI_MERGE_CLEAN2 = UNEMP_RPPI_MERGE_CLEAN.drop(columns=['Age Group_x', 'Sex_x', 'UNIT_x',
                                                               'Statistic_y', 'Age Group_y', 'Sex_y', 'UNIT_y',
                                                               'UNIT', 'UNIT2', 'Type of Residential Property2'])
print(UNEMP_RPPI_MERGE_CLEAN2.shape)
print(UNEMP_RPPI_MERGE_CLEAN2.columns)
print(UNEMP_RPPI_MERGE_CLEAN2.head())
print(UNEMP_RPPI_MERGE_CLEAN2.tail())

# create a new column for unemployment using C19 rate for post March 20 period

for index, row in UNEMP_RPPI_MERGE_CLEAN2.iterrows():
    if UNEMP_RPPI_MERGE_CLEAN2.loc[index, 'VALUE_y'] > 0:
        UNEMP_RPPI_MERGE_CLEAN2.loc[index, 'UNEMP Rate to use'] = row['VALUE_y']
    else:
        UNEMP_RPPI_MERGE_CLEAN2.loc[index, 'UNEMP Rate to use'] = row['VALUE_x']
print(UNEMP_RPPI_MERGE_CLEAN2.head(78))

# create a dictionary to input P&L sensitivity data
sensitivity_RPPI = {"1% RPPI impact": 5.8}
sensitivity_UMEMP = {"1% UNEMP impact": 1.5}
print(sensitivity_RPPI["1% RPPI impact"])
print(sensitivity_UMEMP["1% UNEMP impact"])

# create dataframes from dictionaries
sensitivityRPPIdf = pd.DataFrame.from_dict(sensitivity_RPPI, orient='index', columns=['RPPI'])
sensitivityUMEMPdf = pd.DataFrame.from_dict(sensitivity_UMEMP, orient='index', columns=['UNEMP'])
print(sensitivityRPPIdf)
print(sensitivityUMEMPdf)

# calculate monthly move on Unemployment rate
UNEMP_RPPI_MERGE_CLEAN2['UNEMP_MVMT'] = UNEMP_RPPI_MERGE_CLEAN2['UNEMP Rate to use'].diff()
print(UNEMP_RPPI_MERGE_CLEAN2.tail())

# multiply main dataframe by sensitivities
RPPI_1 = 5.8
UMEMP_1 = 1.5
print(RPPI_1)
print(UMEMP_1)

UNEMP_RPPI_MERGE_CLEAN2['RPPI_1'] = RPPI_1
UNEMP_RPPI_MERGE_CLEAN2['UMEMP_1'] = UMEMP_1

print(UNEMP_RPPI_MERGE_CLEAN2.head())
print(UNEMP_RPPI_MERGE_CLEAN2.columns)

# Calculate P&L impact of RPPI and UNEMP movements monthly

UNEMP_RPPI_MERGE_CLEAN2['RPPI_PL'] = (UNEMP_RPPI_MERGE_CLEAN2['RPPI_1'] * UNEMP_RPPI_MERGE_CLEAN2['VALUE'])/100
UNEMP_RPPI_MERGE_CLEAN2['UNEMP_PL'] = (UNEMP_RPPI_MERGE_CLEAN2['UMEMP_1'] * UNEMP_RPPI_MERGE_CLEAN2['UNEMP_MVMT'])/100
UNEMP_RPPI_MERGE_CLEAN2['TOTAL_PL'] = UNEMP_RPPI_MERGE_CLEAN2['UNEMP_PL'] + UNEMP_RPPI_MERGE_CLEAN2['RPPI_PL']

print(UNEMP_RPPI_MERGE_CLEAN2.tail())
print(UNEMP_RPPI_MERGE_CLEAN2.columns)
UNEMP_RPPI_MERGE_CLEAN2.columns = ['Statistic_x', 'Unemployment', 'Lower and Upper Bound', 'C19_Unemployment',
                                   'Statistic', 'Type of Residential Property', 'RPPI MVMT', 'Statistic2',
                                   'RPPI_INDEX', 'UNEMPLOYMENT RATE', 'UNEMP_MVMT', 'RPPI_1', 'UMEMP_1',
                                   'RPPI_PL', 'UNEMP_PL', 'TOTAL_PL']

UNEMP_RPPI_MERGE_CLEAN2['C19_FLAG'] = np.where(UNEMP_RPPI_MERGE_CLEAN2['C19_Unemployment'] > 0, 'C19', 'Pre_C19')
print(UNEMP_RPPI_MERGE_CLEAN2.columns)

# create scatter graph of unemployment and Property prices

sns.set_theme(style="white")

# Load  dataset
data = UNEMP_RPPI_MERGE_CLEAN2

# Plot unemployment against house prices with other semantics
sns.relplot(x="RPPI_INDEX", y="Unemployment", hue="C19_FLAG",

            sizes=(40, 400), alpha=.5, palette="muted",

            height=6, data=data)
plt.show()

data2 = UNEMP_RPPI_MERGE_CLEAN2.loc["2019M04":"2021M04"]
data3 = data2.reset_index()
print(data3.columns)
print(data3.tail())
m_array = data3["Month"].to_numpy()
r_array = data3["RPPI MVMT"].to_numpy()
u_array = data3["UNEMP_MVMT"].to_numpy()
print(m_array)


# insert line graph with two Y axis


fig, ax1 = plt.subplots()

color = 'tab:red'

ax1.set_xlabel('Month')

ax1.set_ylabel('RPPI MVMT', color=color)

ax1.plot(m_array, r_array, color=color)

ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(-5, 15)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'

ax2.set_ylabel('UNEMP_MVMT', color=color)  # we already handled the x-label with ax1

ax2.plot(m_array, u_array, color=color)

ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.setp(ax1.get_xticklabels(), rotation=45)
plt.show()

# create a bar chart showing P&L impact per month due to macro economic movements during C19
f2, ax2a = plt.subplots(figsize=(4, 3), dpi=100)
# plot a bar chart
ax2 = sns.barplot(
    y="TOTAL_PL",
    x="Month",
    data=data3,
    estimator=sum,
    ci=None,
    color='#69b3a2')
plt.setp(ax2.get_xticklabels(), rotation=90)
ax2.set_ylim(-0.10, 0.25)
plt.show()

f3, ax3a = plt.subplots(figsize=(4, 3), dpi=100)
# plot a bar chart RPPI only
ax3 = sns.barplot(
    y="RPPI_PL",
    x="Month",
    data=data3,
    estimator=sum,
    ci=None,
    color='orange')
plt.setp(ax3.get_xticklabels(), rotation=90)
ax3.set_ylim(-0.10, 0.25)
plt.show()

f4, ax4a = plt.subplots(figsize=(4, 3), dpi=100)
# plot a bar chart UNEMP only
ax4 = sns.barplot(
    y="UNEMP_PL",
    x="Month",
    data=data3,
    estimator=sum,
    ci=None,
    color="purple")
plt.setp(ax4.get_xticklabels(), rotation=90)
ax4.set_ylim(-0.10, 0.25)
plt.show()

# API - Import Latest RPPI Dataset convert to CSV

data4 = requests.get("https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22HPM09%22%7D,%22version%22:%222.0%22%7D%7D")
parsed_data4 = data4.json()
with open("RPPI_API.txt", "w") as outfile:
    json.dump(parsed_data4, outfile)
parsed_data5 = pd.read_json('/Users/macbookpro/PycharmProjects/UCD_HeatherMc/RPPI_API.txt')
RPPI_API_Data = parsed_data5.to_csv('/Users/macbookpro/PycharmProjects/UCD_HeatherMc/RPPI_API.csv')
RPPI_API_Data_df = pd.read_csv('RPPI_API.csv')

# Reusable code

#start_date =
#end_date =
#column_name =


#data5 = UNEMP_RPPI_MERGE_CLEAN2.loc["2020M03":"2021M04"]
#print(data5)

#def Cumulative_Sum(column_name, start_date, end_date):
    #datax=data.loc[start:end]
    #print(datax)

#Cumulative_Sum(UNEMP_RPPI_MERGE_CLEAN2,"2020M03","2021M04")


