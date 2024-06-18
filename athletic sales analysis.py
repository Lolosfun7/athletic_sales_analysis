import pandas as pd

df_2020 = pd.read_csv('athletic_sales_2020.csv')
df_2021 = pd.read_csv('athletic_sales_2021.csv')

print(df_2020.columns)
print(df_2021.columns)
print(df_2020.dtypes)
print(df_2021.dtypes)

combined_df = pd.concat([df_2020, df_2021], axis=0, join='inner').reset_index(drop=True)

print(combined_df.isnull().sum())

print(combined_df.dtypes)

women_footwear_df = combined_df[combined-df['Product'] == "Women's Athletic Footwear"]

women_footwear_df.rename(columns={'Units_Sold': 'Total_Units_Sold'}, inplace=True)

top_retailers = women_footwear_df.groupby(['Retailer', 'Region', 'State', 'City']).agg(Total_Units_Sold=('Total_Units_Sold', 'sum')).sort_values('Total_Units_Sold', ascending=False).head(5)

pivot_table_day = women_footwear.df.pivot_table(index='invoice_date', values='total_sales')

pivot_table_day.rename(colunns={'total_sales': 'Total_Sales'}, inplace=True)

resampled_df = pivot_table_day.resample('D').sum()

top_10_days = resampled_df.sort_values('Totals_Sales', ascending=False).head(10)

resampled_week = pivot_table_day.resample('W').sum()

top_10_weeks = resampled_week.sort_values('Total_Sales', ascending=False).head(10)




