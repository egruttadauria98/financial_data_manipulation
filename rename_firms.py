import pandas as pd

import constants


def new_name_standard(name):
    '''
    Function to rename firms into standard names
    :param name: old name
    :return: new name
    '''

    if 'P&G' in name:
        return 'P&G'

    for p in constants.LIST_PEPSI_VARIANTS:
        if p in name:
            return 'PEPSI-COLA'

    if 'SOUTHERN' in name:
        return 'SOUTHERN NATURAL GAS'
    
    if 'COCA-COLA' in name:
        return 'COCA-COLA'

    if 'TIME WARN' in name:
        return 'TIME WARNER CABLE'

    split = name.split()
    new_name = ''
    for s in split:
        if not s.isnumeric():
            new_name += s
            new_name += ' '
        else:
            break

    for n in constants.LIST_SINGLE_NAME_FIRMS:
        if n in new_name:
            return n

    for n in constants.LIST_DOUBLE_NAME_FIRMS:
        if n in new_name:
            return n

    return new_name.strip()


# RENAME STANDARD NAMES
df = pd.read_csv(constants.PATH_NAMES_STANDARD)
df[constants.NAME_NEW_NAME_COLUMN] = df['Name'].apply(lambda x: new_name_standard(x))
df.to_csv(constants.NAME_MAPPING_STANDARD, index=False)

#######################################################################################


def new_name_spread(name):
    '''
    Extention of the above function to rename firms + if bid or ask data
    :param name: old name bid/ask
    :return: new name bid/ask
    '''

    new_name = new_name_standard(name)
    new_name += ' '
    new_name += name.split()[-1]
    return new_name


# RENAME SPREAD NAMES
df = pd.read_csv(constants.PATH_NAMES_SPREAD)
df[constants.NAME_NEW_NAME_COLUMN] = df['Name'].apply(lambda x: new_name_spread(x))
df.to_csv(constants.NAME_MAPPING_SPREAD, index=False)



