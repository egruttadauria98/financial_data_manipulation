import pandas as pd
import numpy as np

import statsmodels.api as sm

import constants


def upload_result_data(result_path):
    df = pd.read_excel(result_path)
    df = df.set_index(constants.NAME_NEW_NAME_COLUMN)
    df = df.T
    df.index.name = constants.NAME_DATE_COLUMN
    return df


class SimpleRegression:
    df_yield = upload_result_data(constants.NAME_YIELD_FILE)
    risk_free = pd.read_excel(constants.PATH_RISKFREE)

    df_cds = pd.read_excel(constants.PATH_CDS)
    df_cds = df_cds.set_index(constants.NAME_DATE_COLUMN)

    sub_sample = None

    result = dict()

    def __init__(self, firm):
        self.firm = firm

    def get_data_regression(self):

        firm_yield = self.df_yield[self.firm]
        firm_cds = self.df_cds[self.firm]

        df = pd.merge(firm_yield, self.risk_free, on=constants.NAME_DATE_COLUMN)
        df = df.set_index(constants.NAME_DATE_COLUMN)
        df.columns = ['yield', 'risk-free']

        df = pd.merge(df, firm_cds, on=constants.NAME_DATE_COLUMN)
        df.columns = ['yield', 'risk-free', 'X']

        df['y'] = df['yield'] - df['risk-free']

        df.dropna(inplace=True)
        return df

    def data_split(self, df):
        if self.sub_sample is not None:
            df_before = df[:self.sub_sample]
            df_after = df[self.sub_sample:]

            return [df_before, df_after]
        else:
            return [df]

    def fit(self):
        data = self.get_data_regression()
        data_list = self.data_split(data)

        i = 0

        for df in data_list:

            X = np.array(df.X).reshape(-1, 1)
            X = sm.add_constant(X)

            y = np.array(df.y)

            model = sm.OLS(y, X).fit()

            if self.sub_sample is None:
                split = 'NO'
                firm = self.firm
            else:
                split = i
                firm = self.firm + '_' + str(i)

            self.result[firm] = [
                split,
                model.params[0], model.params[1],
                model.tvalues[0], model.tvalues[1],
                model.pvalues[0], model.pvalues[1],
                model.mse_model,
                model.mse_resid,
                model.mse_total,
                model.ssr,
                model.ess,
                model.rsquared,
                model.rsquared_adj,
                model.fvalue,
                model.nobs
            ]

            i += 1

    @classmethod
    def return_data(cls):
        df = pd.DataFrame(cls.result, index=constants.SIMPLE_REGRESSION_COLUMNS).T
        df.to_excel('regression_general.xlsx')

        if cls.sub_sample is not None:
            df_1 = df[df['split'] == 0]
            df_1.to_excel('regression_before.xlsx')

            df_2 = df[df['split'] == 1]
            df_2.to_excel('regression_after.xlsx')


class AdvancedRegression(SimpleRegression):
    df_spread = upload_result_data(constants.NAME_SPREAD_FILE)

    result = dict()

    def __init__(self):
        super().__init__(firm)
        
    def expand_data_regression(self):
        df_simple = self.get_data_regression()

        firm_spread = pd.DataFrame(self.df_spread[self.firm], columns=[self.firm])
        firm_spread = firm_spread.rename(columns={self.firm: 'spread'})
        
        df_advanced = pd.merge(df_simple, firm_spread, on=constants.NAME_DATE_COLUMN)
        df_advanced = df_advanced.rename(columns={'X': 'cds'})

        df_advanced['x1*x2'] = df_advanced['cds'] * df_advanced['spread']

        df_advanced.dropna(inplace=True)
        return df_advanced

    def fit(self):
        data = self.expand_data_regression()
        data_list = self.data_split(data)

        i = 0

        for df in data_list:

            X = df[['cds', 'spread', 'x1*x2']]
            X = np.array(X)#.reshape(-1, 1)
            X = sm.add_constant(X)

            y = np.array(df.y)

            model = sm.OLS(y, X).fit()

            if self.sub_sample is None:
                split = 'NO'
                firm = self.firm
            else:
                split = i
                firm = self.firm + '_' + str(i)

            self.result[firm] = [
                split,
                model.params[0], model.params[1], model.params[2], model.params[3],
                model.tvalues[0], model.tvalues[1], model.tvalues[2], model.tvalues[3],
                model.pvalues[0], model.pvalues[1], model.pvalues[2], model.pvalues[3],
                model.mse_model,
                model.mse_resid,
                model.mse_total,
                model.ssr,
                model.ess,
                model.rsquared,
                model.rsquared_adj,
                model.fvalue,
                model.nobs
            ]

            i += 1

    @classmethod
    def return_data_adv(cls):
        df = pd.DataFrame(cls.result, index=constants.ADV_REGRESSION_COLUMNS).T
        df.to_excel('regression_general_adv.xlsx')

        if cls.sub_sample is not None:
            df_1 = df[df['split'] == 0]
            df_1.to_excel('regression_before_adv.xlsx')

            df_2 = df[df['split'] == 1]
            df_2.to_excel('regression_after_adv.xlsx')


#SimpleRegression.sub_sample = '01/04/2015'
#AdvancedRegression.sub_sample = '01/04/2015'

for firm in constants.PARENT_COMPANIES:

    sr = SimpleRegression(firm)
    sr.fit()

    try:
        ar = AdvancedRegression()
        ar.fit()
    except KeyError:
        pass

SimpleRegression.return_data()
AdvancedRegression.return_data_adv()



