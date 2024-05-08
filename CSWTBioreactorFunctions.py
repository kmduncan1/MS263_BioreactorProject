def fileimport (path='HydraData/'):
    '''
    This is a package for importing .csv files from Central Coast Wetland Group's 2017-2021 12-channel bioreactor experiment and storing them in Pandas dataframes and parses column 3 of each file as UTC dates. 
    
    Parameters
    -------------
    path: string
        The path from the workspace containing the module to the HyrdaData folder excluding the file name.
        Example: '.../MS263_Project/HydraData/'
        Defaults to 'HydraData/' assuming HydraData folder is stored in the same folder as the module for this package.

    Returns
    -------------
    dffb: dataframe
        Dataframe containing fb.csv covering data from the bioreactor forebay.
    dfclist: list
        List containging dataframes for channels 1 through 12 of the bioreactor.
    dfc1: dataframe
        Dataframe for data from channel 1 of the 12-channel bioreactor treatment.
    dfc2: dataframe
        Dataframe for data from channel 2 of the 12-channel bioreactor treatment.
    dfc3: dataframe
        Dataframe for data from channel 3 of the 12-channel bioreactor treatment.
    dfc4: dataframe
        Dataframe for data from channel 4 of the 12-channel bioreactor treatment.
    dfc5: dataframe
        Dataframe for data from channel 5 of the 12-channel bioreactor treatment.
    dfc6: dataframe
        Dataframe for data from channel 6 of the 12-channel bioreactor treatment.
    dfc7: dataframe
        Dataframe for data from channel 7 of the 12-channel bioreactor treatment.
    dfc8: dataframe
        Dataframe for data from channel 8 of the 12-channel bioreactor treatment.
    dfc9: dataframe
        Dataframe for data from channel 9 of the 12-channel bioreactor treatment.
    dfc10: dataframe
        Dataframe for data from channel 10 of the 12-channel bioreactor treatment.
    dfc11: dataframe
        Dataframe for data from channel 11 of the 12-channel bioreactor treatment.
    dfc12: dataframe
        Dataframe for data from channel 12 of the 12-channel bioreactor treatment.
    '''
    #Import Pandas module
    import pandas as pd

    #Read and store data for the forebay in a dataframe and parse dates
    dffb = pd.read_csv(path + 'fb.csv', header=0, na_values='',parse_dates=[2])
    #Create an empty list for bioreactor channel dataframes
    dfclist=[]
    #For loop to read through .csv files labeled c1 through c12
    #Creates a list of dataframes with for the 12 channels of the bioreactor
    for i in range(1,13):
        #Read and store .csv file in a dataframe
        #Append a list of dataframes with bioreactor channels
        dfclist.append(pd.read_csv(path+ '/c' + str(i) + '.csv', header=0, na_values='',parse_dates=[2]))
    #Parse dataframes for inidividual channels contained in dfclist into discrete dataframes
    for i in range(0,12):
        if i==0:
            dfc1=dfclist[i]
        elif i==1:
            dfc2=dfclist[i]
        elif i==2:
            dfc3=dfclist[i]
        elif i==3:
            dfc4=dfclist[i]
        elif i==4:
            dfc5=dfclist[i]
        elif i==5:
            dfc6=dfclist[i]
        elif i==6:
            dfc7=dfclist[i]
        elif i==7:
            dfc8=dfclist[i]
        elif i==8:
            dfc9=dfclist[i]
        elif i==9:
            dfc10=dfclist[i]
        elif i==10:
            dfc11=dfclist[i]
        elif i==11:
            dfc12=dfclist[i]

    return(dffb,dfclist,dfc1,dfc2,dfc3,dfc4,dfc5,dfc6,dfc7,dfc8,dfc9,dfc10,dfc11,dfc12)

def timewindow (df, begin, end):
    '''Creates a sub-dataframe focusing on a discrete, specified time window when given a dataframe with starting and ending unix times. Requires Pandas Python package.

    Parameters
    -----------
    df: dataframe
        Original Pandas dataframe to parse into a smaller timeseries.
    begin: int
        Unix time string indicating the start of the timeseries to be isolated.
    end: int
        Unix time string indicating the end of the timeseries to be isolated.
        
    Returns
    -----------
    dfsub: dataframe
        New Pandas sub-dataframe defined by beginning and ending unix times.
    '''
    import pandas as pd
    ii = (begin <= df['unix_time']) & (df['unix_time'] <= end) 
    dfsub = df[ii]
    
    return(dfsub)
    
def dfclean (dataframe,var='nitrate'):
    '''Creates a sub-dataframe from a provided dataframe with rows containing no values or negative values removed. Requires numpy and pandas.
    
    Parameters
    -------------
    dataframe: dataframe
        Provided Pandas  
    var: string
        Column for nitrogen values. Either 'nitrate', 's_nitrate', or 's_nitrogen' for CCWG bioreactor data. Defaults to 'nitrate'.

    Returns
    -------------
    dfcleaned: dataframe
        Data frame with rows containing negative values or no values removed.
    '''
    import numpy as np
    import pandas as pd
    df = dataframe
    ii_finite = (np.isfinite(df[var])) & (np.isfinite(df['temp'])) & (np.isfinite(df['cond'])) & (np.isfinite(df['sal'])) & (np.isfinite(df['hdo'])) & (np.isfinite(df['sat'])) & (np.isfinite(df['phv'])) & (np.isfinite(df['ph']))
    dffinite = df[ii_finite]
    ii_positive = (0<=dffinite[var]) & (0<=dffinite['temp']) & (0<=dffinite['cond'])& (0<=dffinite['sal']) & (0<=dffinite['hdo']) & (0<=dffinite['sat']) & (0<=dffinite['phv']) & (0<=dffinite['ph'])
    dfcleaned = dffinite[ii_positive]
    return(dfcleaned)

def dfclean_nitratetemp (dataframe,var='nitrate'):
    '''Creates a sub-dataframe from a provided dataframe with rows containing no values or negative values removed for nitrogen and temperature columns. Requires numpy and pandas.
    
    Parameters
    -------------
    dataframe: dataframe
        Provided Pandas  
    var: string
        Column for nitrogen values. Either 'nitrate', 's_nitrate', or 's_nitrogen' for CCWG bioreactor data. Defaults to 'nitrate'.

    Returns
    -------------
    dfcleanednt: dataframe
        Data frame with rows containing negative values or no values removed for nitrogen and temperture columns.
    '''
    import numpy as np
    import pandas as pd
    df = dataframe
    ii_finite = (np.isfinite(df[var])) & (np.isfinite(df['temp']))
    dffinite = df[ii_finite]
    ii_positive = (0<=dffinite[var]) & (0<=dffinite['temp'])
    dfcleanednt = dffinite[ii_positive]
    return(dfcleanednt)

def BioreactorPCA(df,varlist=['temp','cond','sal','nitrate','hdo','sat','phv','ph']):
    '''Function to calculate eigenvalues, eigenvectors, principle component scores, percent variance accounted for by PC1 and PC2, PC factor loading matrix, and PC scores from a list of variables for a given pandas dataframe.
        Parameters
    -------------
    df: dataframe
        The path from the workspace containing the module to the HyrdaData folder excluding the file name.
        Example: '.../MS263_Project/HydraData/'
        Defaults to 'HydraData/' assuming HydraData folder is stored in the same folder as the module for this package.
    varlist: list
        List of variables to use for PCA. Defaults to short_vars = ['temp','cond','sal','nitrate','hdo','sat','phv','ph'].

    Returns
    -------------
    datamatrix_zscore, evalues_sorted, evectors_sorted, PC1_pvar, PC2_pvar, FactorMatrix, PCscores, TimeMatrix
    datamatrix_zscore: matrix
        Matrix of z-scores for the data matrix.
    evalues_sorted: matrix
        Matrix of eigenvalues sorted by highest to least variance accounted for by PC.
    evectors_sorted: matrix
        Matrix of eigenvectors sorted by highest to least variance accounted for by PC.
    PC1_pvar: float
        Percentage of variance in the data accounted for by PC1.
    PC2_pvar: dataframe
        Percentage of variance in the data accounted for by PC2.
    FactorMatrix: matrix
        Factor loading matrix for the data matrix with PC's sorted so that ordering follows PC1, PC2,...PCn by column.
    PCscores: matrix
        Matrix of principle component scores sorted so that ordering follows PC1, PC2,...PCn by column.
    TimeMatrix: matrix
        Matrix of UTC times for the given dataframe to be used for plotting principle component score timeseries.
    '''
    #Import packages and modules
    import pandas as pd
    import numpy as np
    from scipy import linalg
    
    dfmatrixscaffold = pd.DataFrame() #Create a scaffold to hold values for creating a matrix
    #Populate matrix with values for variables from the given dataframe from  varlist
    for x in varlist:
       dfmatrixscaffold[x] = df[x]
    
    datamatrix = dfmatrixscaffold.values  #Create datamatrix from values contained in dfmatrixscaffold
    datamatrix_zscore = (datamatrix- np.mean(datamatrix, axis=0))/np.std(datamatrix,axis=0, ddof=1) #Calculate z-scores from the data matrix
    
    corr_matrix = np.cov(datamatrix_zscore, rowvar=False) #Create a correlation matrix
    evalues, evectors = linalg.eig(corr_matrix) #Calculate eigenvalues and eigenvectors
    
    #Sort eigenvalues and eigenvectors by decreasing variance (PC1 first, PC2 second, etc)
    idx = evalues.argsort()[::-1]  
    evalues_sorted = evalues[idx]
    evectors_sorted = evectors[:,idx]

    realvalues = np.real(evalues_sorted) #Convert eigenvalues to real numbers 
    percent_variance = realvalues/np.sum(realvalues)*100 #Create a matrix with the percentage of variables PC's account for
    PC1_pvar = percent_variance[0] #Extract percent variance for PC1
    PC2_pvar = percent_variance[1] #Repeat for PC2

    LambdaMatrix = np.diag(realvalues) #Create a lambda matrix with eigenvalues distributed diagonally
    FactorMatrix = evectors@(LambdaMatrix**0.5) #Create a factor loading matrix
    
    PCscores = datamatrix_zscore@evectors_sorted #Calculate principle component scores
    TimeMatrix = df['utc_time'].values  #Creates a time matrix for plotting PC scores
    
    return(datamatrix_zscore, evalues_sorted, evectors_sorted, PC1_pvar, PC2_pvar, FactorMatrix, PCscores, TimeMatrix)