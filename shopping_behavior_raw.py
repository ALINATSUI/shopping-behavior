import pandas as pd 
df = pd.read_csv('data/raw/shopping.csv')
# pd.set_option('display.max_columns', None)
print(df.head(25))

print(f'\nDescriptive Stats: \n\n',round(df.describe()))
print(f'\nShape: ', df.shape)
print(f'\nInfo: ', df.info())
print(df.describe())

