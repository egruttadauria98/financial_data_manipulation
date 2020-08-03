import pandas as pd

import constants

mapping = pd.read_csv(constants.NAME_MAPPING_STANDARD)
df_yield_raw = pd.read_excel(constants.PATH_BOND_YIELD)

df_yield = pd.merge(mapping, df_yield_raw, on='Name')
df_yield.drop_duplicates(['ISIC code'], inplace=True)

#df_yield.to_excel('merge_yield.xlsx')

df_yield.drop(['Name'], axis=1, inplace=True)
result = df_yield.groupby(['new_name']).mean()
result.to_excel(constants.NAME_YIELD_FILE)


