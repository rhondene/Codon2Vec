# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:13:36 2021

@author: RWint
"""

import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)



def preproc_exprs_matrix(exprs_matrix, exprs_percentile):
    
    """Accepts expression table and filters the genes in the top and bottom X percentile of expression """
    
    ####---------------quick detect whether table format is csv or tsv
    sample = pd.read_table(exprs_matrix, sep='\t', nrows=3)
    if sample.shape[1]>1:
        df_exprs = pd.read_table(exprs_matrix, sep='\t' )
    else:
        df_exprs = pd.read_table(exprs_matrix, sep=',')
    
    del sample
    #Checkpoint: expression table must have at least 2 columns with seqs IDs and their expression values
    print(df_exprs.shape, '\n\n')
    assert df_exprs.shape[1]>1,'SizeError: Expression table must have at least 2 columns.'
   
    
    #retain first 2 cols and drop unused to reduce space 
    cols = df_exprs.columns
    df_exprs= df_exprs[cols[:2]]
     
    #ensure that the ID column (1st column is type string)
    df_exprs[cols[0]]= df_exprs[cols[0]].astype(str)
    #1. sort values by exprs. Assume that relative expression is the 2nd column
    df_exprs.sort_values(by=cols[1], ascending=True)
    #remove zero-valued expression 
    df_exprs=df_exprs[ df_exprs[ cols[1] ]> 0.0]
    
    #2. ##determine training quantiles cut-off 
    
     ##choose top_10 and bottom exprs_10
    lower = df_exprs[cols[1] ].quantile(exprs_percentile)
    upper = df_exprs[cols[1] ].quantile(1-exprs_percentile)
    
    #3. extract top and bottom percentile
    bottom = df_exprs[df_exprs[cols[1]]<lower]
    top= df_exprs[df_exprs[cols[1]]>upper] 
    top['Exprs_Level'] = 'High'
    bottom['Exprs_Level'] = 'Low'
    #combine the top and bottom exprs
    trunc_exprs= pd.concat([top,bottom], axis=0)
    
    
    
    return trunc_exprs

if __name__=='__main__':
    preproc_exprs_matrix(exprs_matrix, sep)
    
