def BR_fileimport (path='HydraData/'):
    '''
    This is a package for importing .csv files from Central Coast Wetland Group's 
    2017-2021 12-channel bioreactor experiment and storing them in Pandas dataframes.
    Appends all data frames with UTC dates and times converted from unix time. 
    
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
        Appended with UTC dates and times converted from unix time.
    dfclist: list
        List containging dataframes for channels 1 through 12 of the bioreactor.
        Dataframes are appended with UTC dates and times converted from unix time.
    '''
    #Import Pandas module
    import pandas as pd

    #Read and store data for the forebay in a dataframe
    dffb = pd.read_csv(path + 'fb.csv', header=0, na_values='')
    #Create a column for UTC dates and times converted from unix times in the forebay dataframe
    dffb['utc_datetime']=pd.to_datetime(dffb['unix_time'], unit='s')
    #Create an empty list for bioreactor channel dataframes
    dfclist=[]
    #For loop to read through .csv files labeled c1 through c12
    #Creates a list of dataframes with for the 12 channels of the bioreactor
    for i in range(1,13):
        #Read and store .csv file in a dataframe
        #Append a list of dataframes with bioreactor channels
        dfclist.append(pd.read_csv(path+ '/c' + str(i) + '.csv', header=0, na_values=''))
    #Create a column for UTC dates and times converted from unix times in each dataframe
    for df in dfclist:
        df['utc_datetime']=pd.to_datetime(df['unix_time'], unit='s')
    return(dffb,dfclist)

def BR_ParseChannels (dfclist):
    '''
    This package isolates dataframes for individual bioreactor channels 
    from the dfclist created using the CSWTBioreactorFunctions.BR_filimport function.
    
    Parameters
    -----------
    dfclist: list
        List containging dataframes for channels 1 through 12 of the bioreactor.

    Returns
    -----------
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
    return(dfc1,dfc2,dfc3,dfc4,dfc5,dfc6,dfc7,dfc8,dfc9,dfc10,dfc11,dfc12)

