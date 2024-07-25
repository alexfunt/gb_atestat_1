import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Оригинальный DataFrame:")
data.head()
print(data)

unique = data['whoAmI'].unique()
one_hot_df = pd.DataFrame()

for value in unique:
    one_hot_df[value] = data['whoAmI'].apply(lambda x: True if x == value else False)

print("One-hot DataFrame")
one_hot_df.head()
print(one_hot_df)
