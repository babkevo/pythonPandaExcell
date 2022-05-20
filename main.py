import pandas as pd
import plotly.express as px

df_gold_prices = pd.read_csv('annual_gold-prices.csv.csv')

# viewing the data
print(df_gold_prices.tail(10))

dates = df_gold_prices['Date']
prices = df_gold_prices['Price']

df_gold_prices['buy_price'] = prices * .9
print(df_gold_prices['Price'].max())
df_gold_prices['Date'] = df_gold_prices['Date'].str.replace('-', '/')

print(df_gold_prices)

# Drawing a graph

fig = px.line(df_gold_prices, x=dates, y=prices, title='Gold prices in Graph' )
fig.show()