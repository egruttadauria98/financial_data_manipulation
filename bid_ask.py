import pandas as pd

import constants

mapping = pd.read_csv(constants.NAME_MAPPING_SPREAD)

mapping_standard = pd.read_csv(constants.NAME_MAPPING_STANDARD)
list_names = list(mapping_standard.new_name)

df_spread_raw = pd.read_excel(constants.PATH_BID_ASK)

df_spread = pd.merge(mapping, df_spread_raw, on='Name')
df_spread.drop_duplicates(['ISIC code'], inplace=True)

#result.to_excel('merge_bid_ask.xlsx')

df_spread.drop(['Name', 'ISIC code'], axis=1, inplace=True)
df_spread.iloc[:, 1:] = df_spread.iloc[:, 1:].astype('float64')

df_spread = df_spread.groupby([constants.NAME_NEW_NAME_COLUMN]).mean().T


def get_spread(row):
    bid = float(row['bid'])
    ask = float(row['ask'])
    mid = (bid + ask)/2
    spread = ((ask - bid)/mid)*100
    return spread


final_df = pd.DataFrame()

for i in range(0, 1500, 2):
    try:
        p = df_spread.iloc[:, [i, i+1]]
        name_col = ' '.join(p.columns[0].split()[:-1])
        p.columns = ['ask', 'bid']
        final_df[name_col] = p.apply(lambda x: get_spread(x), axis=1)

    except IndexError:
        print('Overflow')
        break

final_df = final_df.T
final_df.index.name = constants.NAME_NEW_NAME_COLUMN

final_df.to_excel(constants.NAME_SPREAD_FILE)



