import pandas as pd
import plotly.express as px
import requests

# Read in the World Bank dataset
url = "https://api.worldbank.org/v2/countries/all/indicators/NY.GDP.PCAP.CD?format=json"
data = requests.get(url).json()
df = pd.json_normalize(data[1])

# prompt the user to enter the country names
country1 = input("Enter the first country name: ")
country2 = input("Enter the second country name: ")
country3 = input("Enter the third country name: ")

if country1.upper() not in df['country.value'].str.upper().unique():
    print(f'{country1} is not in the dataset, please enter a valid country name')
elif country2.upper() not in df['country.value'].str.upper().unique():
    print(f'{country2} is not in the dataset, please enter a valid country name')
elif country3.upper() not in df['country.value'].str.upper().unique():
    print(f'{country3} is not in the dataset, please enter a valid country name')
else:
    pass
# Filter the dataset to include only the selected countries and indicator
df_country1 = df[(df['country.value'] == country1)]
df_country2 = df[(df['country.value'] == country2)]
df_country3 = df[(df['country.value'] == country3)]

# Create a line chart to visualize the GDP per capita over time for multiple countries
fig = px.line(df_country1, x='date', y='value', title='GDP per capita in ' + country1)
fig.add_scatter(x=df_country2['date'], y=df_country2['value'], name=country2)
fig.add_scatter(x=df_country3['date'], y=df_country3['value'], name=country3)
fig.show()

# Merging the datasets and creating scatter plots to analyze the relationship between GDP per capita and other indicators
unemployment_url = "https://api.worldbank.org/v2/countries/all/indicators/SL.UEM.TOTL.ZS?format=json"
unemployment_data = requests.get(unemployment_url).json()
unemployment_df = pd.json_normalize(unemployment_data[1])
merged_df_country1 = pd.merge(df_country1, unemployment_df, left_on=["country.value","date"], right_on=["country.value","date"], how="inner")
merged_df_country2 = pd.merge(df_country2, unemployment_df, left_on=["country.value","date"], right_on=["country.value","date"], how="inner")
merged_df_country3 = pd.merge(df_country3, unemployment_df, left_on=["country.value","date"], right_on=["country.value","date"], how="inner")
fig = px.scatter(merged_df_country1, x='value_x', y='value_y',title='GDP per capita vs Unemployment Rate')
fig.add_scatter(x=merged_df_country2['value_x'], y=merged_df_country2['value_y'], name=country2)
fig.add_scatter(x=merged_df_country3['value_x'], y=merged_df_country3['value_y'], name=country3)


# it seems that the api i am using does not suit the needs of this program.
# please go on the internet and find a valid data file for GDP.
# find an api, or a data set and download as a csv file for the program to
# read directly
