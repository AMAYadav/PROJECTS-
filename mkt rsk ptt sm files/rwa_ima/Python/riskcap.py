import numpy as np
import pandas as pd
from scipy.stats import norm

class VaR():

    def __init__(self, sensitivities, risk_factor_prices,  
                 horizon = 1, methodology = 'historical', confidence = 0.95 ):
    
        ''' Calculates value-at-risk for a portfolio of securities using parametric or historical method as specified 
    
        parameters
        ----------
        sensitivities : (pd.DataFrame) 
    
        The number of rows is same as number of instruments (m)
        The number of columns is same as number of risk factors (n)
        The values correspond to the dollar sensitivity of ith instrument to jth risk factor 
    
        risk_factor_prices : (pd.DataFrame)

        Risk factors prices timeseries (T x n) where T is the length of the timeseries and n is number of risk factors

        horizon : (int)

        Captures the liquidity horizon to be used in capital calculation. 
        Default value is 1 day for all risk factors

        methodology : (string)

        specify 'historical'(default) or 'parametric' as needed 
        parametric method assumes multivariate normal distribution of risk factors

        confidence : (float) 

        Specifies confidence interval to be used. Default value is 95%
        Typical choices are 95%, 99%, 99.9%
        
        Returns
        -------
        A single number for Value-at-risk Capital

        '''
        
        # obtain timeseries length(T), number of risk factors(n) and number of instruments(m)
       
        self.no_of_factors = risk_factor_prices.shape[1]
        self.no_of_obs = risk_factor_prices.shape[0]
        self.no_of_instruments = sensitivities.shape[0]
        self.confidence = confidence
        self.methodology = methodology
        self.horizon = horizon
        self.sensitivities = sensitivities
        self.prices = risk_factor_prices
        
    def fit(self):
        
        self.net_sensitivities = (self.sensitivities).sum(axis=0)       # Netting sensitivities on the same risk factor

        
        if self.methodology == 'historical':
            
            self.ret = (self.prices).pct_change(self.horizon).dropna()
            self.PnL = (self.ret)@(self.net_sensitivities.T)         # Portfolio PnL timeseries
            self.VaR = abs((self.PnL).quantile(1-self.confidence))
            
        elif self.methodology == 'parametric':
            
            R = (self.prices).pct_change().dropna()
            W = (self.net_sensitivities)
               
            Cov = R.cov()*self.horizon
            self.sigma = np.sqrt(W.T@Cov@W)
            self.VaR = abs(self.sigma*norm.ppf(1-self.confidence)).squeeze()
            

class ES():

    def __init__(self, sensitivities, risk_factor_prices,  
                 horizon = 1, methodology = 'historical', confidence = 0.95 ):
    
        ''' Calculates Expected Shortfall for a portfolio of securities using parametric or historical method as specified 
    
        parameters
        ----------
        sensitivities : (pd.DataFrame) 
    
        The number of rows is same as number of instruments (m)
        The number of columns is same as number of risk factors (n)
        The values correspond to the dollar sensitivity of ith instrument to jth risk factor 
    
        risk_factor_prices : (pd.DataFrame)

        Risk factors prices timeseries (T x n) where T is the length of the timeseries and n is number of risk factors

        horizon : (int)

        Captures the liquidity horizon to be used in capital calculation. 
        Default value is 1 day for all risk factors

        methodology : (string)

        specify 'historical'(default) or 'parametric' as needed 
        parametric method assumes multivariate normal distribution of risk factors

        confidence : (float) 

        Specifies confidence interval to be used. Default value is 95%
        Typical choices are 95%, 99%, 99.9%
        
        Returns
        -------
        A single number for Value-at-risk Capital

        '''
        
        # obtain timeseries length(T), number of risk factors(n) and number of instruments(m)
       
        self.no_of_factors = risk_factor_prices.shape[1]
        self.no_of_obs = risk_factor_prices.shape[0]
        self.no_of_instruments = sensitivities.shape[0]
        self.confidence = confidence
        self.methodology = methodology
        self.horizon = horizon
        self.sensitivities = sensitivities
        self.prices = risk_factor_prices
        
    def fit(self):
        
        self.net_sensitivities = (self.sensitivities).sum(axis=0)       # Netting sensitivities on the same risk factor

        
        if self.methodology == 'historical':
            
            self.ret = (self.prices).pct_change(self.horizon).dropna()
            self.PnL = ((self.ret)@(self.net_sensitivities.T)).to_frame(name = 'PnL')         # Portfolio PnL timeseries
            self.ES = abs((self.PnL[self.PnL['PnL'] < self.PnL['PnL'].quantile(1-self.confidence)]).mean()).squeeze()
            
        elif self.methodology == 'parametric':
            
            R = (self.prices).pct_change().dropna()
            W = (self.net_sensitivities)
               
            Cov = R.cov()*self.horizon
            self.sigma = np.sqrt(W.T@Cov@W)
            self.ES = abs((self.sigma)*norm.pdf(norm.ppf(1-self.confidence))/(1-self.confidence)).squeeze()
            
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy import stats

class VaR():

    def __init__(self, sensitivities, risk_factor_prices,  
                 horizon = 1, methodology = 'historical', confidence = 0.95 ):
    
        ''' Calculates value-at-risk for a portfolio of securities using parametric or historical method as specified 
    
        parameters
        ----------
        sensitivities : (pd.DataFrame) 
    
        The number of rows is same as number of instruments (m)
        The number of columns is same as number of risk factors (n)
        The values correspond to the dollar sensitivity of ith instrument to jth risk factor 
    
        risk_factor_prices : (pd.DataFrame)

        Risk factors prices timeseries (T x n) where T is the length of the timeseries and n is number of risk factors

        horizon : (int)

        Captures the liquidity horizon to be used in capital calculation. 
        Default value is 1 day for all risk factors

        methodology : (string)

        specify 'historical'(default) or 'parametric' as needed 
        parametric method assumes multivariate normal distribution of risk factors

        confidence : (float) 

        Specifies confidence interval to be used. Default value is 95%
        Typical choices are 95%, 99%, 99.9%
        
        Returns
        -------
        A single number for Value-at-risk Capital

        '''
        
        # obtain timeseries length(T), number of risk factors(n) and number of instruments(m)
       
        self.no_of_factors = risk_factor_prices.shape[1]
        self.no_of_obs = risk_factor_prices.shape[0]
        self.no_of_instruments = sensitivities.shape[0]
        self.confidence = confidence
        self.methodology = methodology
        self.horizon = horizon
        self.sensitivities = sensitivities
        self.prices = risk_factor_prices
        
    def fit(self):
        
        self.net_sensitivities = (self.sensitivities).sum(axis=0)       # Netting sensitivities on the same risk factor

        
        if self.methodology == 'historical':
            
            self.ret = (self.prices).pct_change(self.horizon).dropna()
            self.PnL = (self.ret)@(self.net_sensitivities.T)         # Portfolio PnL timeseries
            self.VaR = abs((self.PnL).quantile(1-self.confidence))
            
        elif self.methodology == 'parametric':
            
            R = (self.prices).pct_change().dropna()
            W = (self.net_sensitivities)
               
            Cov = R.cov()*self.horizon
            self.sigma = np.sqrt(W.T@Cov@W)
            self.VaR = abs(self.sigma*norm.ppf(1-self.confidence)).squeeze()
            

class ES():

    def __init__(self, sensitivities, risk_factor_prices,  
                 horizon = 1, methodology = 'historical', confidence = 0.95 ):
    
        ''' Calculates Expected Shortfall for a portfolio of securities using parametric or historical method as specified 
    
        parameters
        ----------
        sensitivities : (pd.DataFrame) 
    
        The number of rows is same as number of instruments (m)
        The number of columns is same as number of risk factors (n)
        The values correspond to the dollar sensitivity of ith instrument to jth risk factor 
    
        risk_factor_prices : (pd.DataFrame)

        Risk factors prices timeseries (T x n) where T is the length of the timeseries and n is number of risk factors

        horizon : (int)

        Captures the liquidity horizon to be used in capital calculation. 
        Default value is 1 day for all risk factors

        methodology : (string)

        specify 'historical'(default) or 'parametric' as needed 
        parametric method assumes multivariate normal distribution of risk factors

        confidence : (float) 

        Specifies confidence interval to be used. Default value is 95%
        Typical choices are 95%, 99%, 99.9%
        
        Returns
        -------
        A single number for Value-at-risk Capital

        '''
        
        # obtain timeseries length(T), number of risk factors(n) and number of instruments(m)
       
        self.no_of_factors = risk_factor_prices.shape[1]
        self.no_of_obs = risk_factor_prices.shape[0]
        self.no_of_instruments = sensitivities.shape[0]
        self.confidence = confidence
        self.methodology = methodology
        self.horizon = horizon
        self.sensitivities = sensitivities
        self.prices = risk_factor_prices
        
    def fit(self):
        
        self.net_sensitivities = (self.sensitivities).sum(axis=0)       # Netting sensitivities on the same risk factor

        
        if self.methodology == 'historical':
            
            self.ret = (self.prices).pct_change(self.horizon).dropna()
            self.PnL = ((self.ret)@(self.net_sensitivities.T)).to_frame(name = 'PnL')         # Portfolio PnL timeseries
            self.ES = abs((self.PnL[self.PnL['PnL'] < self.PnL['PnL'].quantile(1-self.confidence)]).mean()).squeeze()
            
        elif self.methodology == 'parametric':
            
            R = (self.prices).pct_change().dropna()
            W = (self.net_sensitivities)
               
            Cov = R.cov()*self.horizon
            self.sigma = np.sqrt(W.T@Cov@W)
            self.ES = abs((self.sigma)*norm.pdf(norm.ppf(1-self.confidence))/(1-self.confidence)).squeeze()
            
class Validation():
    
    def __init__(self, data):
        
        '''Calculates Backtesting results using FRTB prescribed approach
        
        parameters
        ---------
        data : (pd.DataFrame)
        Must contain timeseries data of exactly 250 observations under columns labeled 'APL' and 'HPL' and 'VaR'
        VaR timeseries must be 1-day 99% against which APL and HPL will be backtested. 
        
        
        '''
        self.data = data
        
    def fit(self):
        
        if (self.data).shape[0] != 250:
            print('Number of observations must be 250')
            
        else:
            
            self.APL_exceedances = (-self.data[(self.data)['APL'] > (self.data)['VaR']]).shape[0]
            self.HPL_exceedances = (-self.data[(self.data)['HPL'] > (self.data)['VaR']]).shape[0]
            self.exceedances = max(self.APL_exceedances,self.HPL_exceedances)
            
            if self.exceedances <= 4:
                self.BT_zone = 'Green'
                self.multiplier = 1.50
                
            elif self.exceedances == 5:
                self.BT_zone = 'Amber'
                self.multiplier = 1.70
                
            elif self.exceedances == 6:
                self.BT_zone = 'Amber'
                self.multiplier = 1.76
                
            elif self.exceedances == 7:
                self.BT_zone = 'Amber'
                self.multiplier = 1.83
                
            elif self.exceedances == 8:
                self.BT_zone = 'Amber'
                self.multiplier = 1.88
                
            elif self.exceedances == 9:
                self.BT_zone = 'Amber'
                self.multiplier = 1.92
                
            else:
                self.BT_zone = 'Red'
                self.multiplier = 2
                
        self.spearman_corr = stats.spearmanr((self.data)['HPL'], (self.data)['RTPL'])[0]
        self.KS = stats.ks_2samp((self.data)['HPL'], (self.data)['RTPL'])[0]
        
        if self.spearman_corr > 0.8 and self.KS < 0.09:
            self.PLAT_zone = 'Green'
            
        elif self.spearman_corr < 0.7 or self.KS > 0.12:
            self.PLAT_zone = 'Red'
            
        else:
            self.PLAT_zone = 'Amber'
            
    def summary(self):
        
        df1 = pd.DataFrame(data = [[self.APL_exceedances, self.HPL_exceedances, 
                                  self.exceedances, self.BT_zone, self.multiplier]], 
                          columns = ['(Exceedances #)APL', '(Exceedances #)HPL',
                                     '(Exceedances #)Max', 'Zone', 'Multiplier'])
        
        df2 = pd.DataFrame(data = [[self.spearman_corr, self.KS, self.PLAT_zone]], 
                          columns = ['spearman correl', 'KS', 'Zone'] )
        
        print('Backtesting results:')
        display(df1)
        
        print('PLAT results:')
        display(df2)
                 