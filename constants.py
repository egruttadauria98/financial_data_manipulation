
# RENAME FIRMS
LIST_SINGLE_NAME_FIRMS = ['AT&T', 'BELLSOUTH', 'CONOCOPHILLIPS', 'COMCAST', 'DOW', 'DUKE', 'EXELON', 'FORD', 'MERCK', 'VERIZON']
LIST_DOUBLE_NAME_FIRMS = ['EL PASO', 'KINDER MORGAN']
LIST_PEPSI_VARIANTS = ['PEPCO', 'PEPSI-COLA', 'PEPSICO']

PATH_NAMES_STANDARD = 'name_mapping/old/firms_standard.csv'
PATH_NAMES_SPREAD = 'name_mapping/old/firms_spread.csv'

NAME_MAPPING_STANDARD = 'name_mapping_standard.csv'
NAME_MAPPING_SPREAD = 'name_mapping_spread.csv'

NAME_NEW_NAME_COLUMN = 'new_name'

# AVERAGE YIELD
PATH_BOND_YIELD = 'data/bond_yields.xlsx'

# BID ASK
PATH_BID_ASK = 'data/bid_ask.xlsx'

# REGRESSION

PARENT_COMPANIES = ['3M COMPANY', 'ABBOTT LABORATORIES', 'ALTRIA GROUP INCO',
                    'AMGEN INCORPORATED', 'AT&T', 'THE BOEING COMPANY',
                    'BRISTOL-MR.SQUIBB', 'CATERPILLAR INCO', 'CISCO SYSTEMS INCO.',
                    'COCA-COLA', 'COLGATE-PALMOLIVE', 'COMCAST', 'CONOCOPHILLIPS',
                    'DOW', 'ELI LILLY AND CO.', 'EMERSON ELEC.CO.', 'EXELON',
                    'FEDEX CORPORATION', 'FORD', 'GENERAL ELEC CO', 'THE HOME DEPOT',
                    'HONEYWELL INTL', 'INTL BUS MCHS CORP', 'JOHNSON & JOHNSON',
                    'LOCKHEED MARTIN', 'LOWE S COS.INCO.', 'MCDONALD S CORP.',
                    'MEDTRONIC INCO', 'MICROSOFT CORP', 'OCCIDENT PTL CORP',
                    'PEPSI-COLA', 'PFIZER INCO', 'P&G', 'RAYTHEON CO.',
                    'SOUTHERN NATURAL GAS', 'UNION PACIFIC CORP.', 'UNITED PARCEL SER',
                    'UNITED TECHNOLOGIES', 'WALMART INCO.']

SIMPLE_REGRESSION_COLUMNS = [
    'split',
    'coef_const', 'coef_x1',
    't_val_const', 't_val_x1',
    'p_val_const', 'p_val_x1',
    'mse_model', 'mse_resid', 'mse_total',
    'ssr', 'sse',
    'r2', 'r2_adj',
    'f_value',
    'number_obs'
]

ADV_REGRESSION_COLUMNS = [
    'split',
    'coef_const', 'coef_x1', 'coef_x2', 'coef_x3',
    't_val_const', 't_val_x1', 't_val_x2', 't_val_x3',
    'p_val_const', 'p_val_x1', 'p_val_x2', 'p_val_x3',
    'mse_model', 'mse_resid', 'mse_total',
    'ssr', 'sse',
    'r2', 'r2_adj',
    'f_value',
    'number_obs'
]


PATH_RISKFREE = 'data/risk_free.xls'
PATH_CDS = 'data/CDS.xlsx'

NAME_YIELD_FILE = 'results/average_yield.xlsx'
NAME_SPREAD_FILE = 'results/average_spread.xlsx'

NAME_NEW_NAME_COLUMN = 'new_name'
NAME_DATE_COLUMN = 'date'
