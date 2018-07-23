### LOAD TO HAVE PRE-MADE FUNCTIONS FOR JUPYTER NOTEBOOKS THAT WILL NEED EDA, STATS, MODEL EVAL, ETC. ON DATAFRAMES.
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression

def null_checker(df):
    """Takes in dataframe and returns sorted list (descending) of columns with null values, and how many.
    """
    null_columns=df.columns[df.isnull().any()]
    return df[null_columns].isnull().sum().sort_values(ascending=False)

def sample_means(population, n=30, k=1000):
    """Requires numpy. Takes in population and returns list of sample means
    n = sample size
    k = total number of samples
    """
    #import numpy as np
    sample_means = []

    for i in range(k):
        sample = np.random.choice(population, size=n, replace=True)
        sample_means.append(np.mean(sample))

    return sample_means


def confidencer(sample, sd=0.95):
    """Requires scipy.stats. Take in sample and sig. level, then return CI
    sample = dataset
    sd = significance level, default 95%."""

    zscore = stats.norm.ppf(1-(1-sd)/2) 
    
    low_ci = sample.mean() - zscore*sample.sem()

    high_ci = sample.mean() + zscore*sample.sem()
    
#     interval = (low_ci, high_ci)
#     print((low_ci, high_ci))

#     print("{0:.0f}% of similar sample means will fall between the range above.".format(sd*100))
    return (low_ci, high_ci)



def eda(df):
    """For initial EDA of dataframe"""
    print('Dataframe shape',df.shape)
    print('Number of null values: {}'.format(df.isnull().sum().sum()))
    print()
    print(df.info())
    print()
    print(df.describe().T[['mean', 'std', 'min','max']])



def r2_adj(X,y):
    """Requires sklearn regression package + sklearn.metrics
    Returns adjusted R^2 for a model.
    X = predictors
    y = target variable"""
    

    lm = LinearRegression()
    model = lm.fit(X,y)
    
    n = X.shape[0]
    k = X.shape[1]
    r2 = metrics.r2_score(y, model.predict(X))
    
    r2_adj = 1 - (((1-r2)*(n-1))/(n-k-1))
    
    return r2_adj


def metrics_dump(X,y):
    """Requires sklearn regression + sklearn.metrics
    Returns 6 most common model eval scores.
    X = predictors
    y - target variable"""


    lm = LinearRegression()
    lm.fit(X,y)
    y_hat = lm.predict(X)
    
    print('MSE:',metrics.mean_squared_error(y, y_hat))
    print('RMSE:',metrics.mean_squared_error(y, y_hat)**0.5)
    print('MedAE:',metrics.median_absolute_error(y, y_hat))
    print('MAE:',metrics.mean_absolute_error(y, y_hat))
    print('R^2:',metrics.r2_score(y, y_hat))
    print('Adj. R^2:',r2_adj(X,y))
