# -*- coding: utf-8 -*-
"""
@author: RWint
"""
import random
import pandas as pd
import fasta2dict  # custom module to preprocess fasta
from filterExprs import preproc_exprs_matrix as pem #custom module to preprocess expression table
from sklearn.utils import shuffle



def prepare_training_data(exprs_matrix, CDS, exprs_percentile,seed_num):
    """
    Combines expression values and corresponding coding sequences for model input
    Input:
        exprs_matrix: path to expression table
        sep : delimiter of expression table
        CDS: path to fasta file with the cds
    Returns
    df_train: dataframe for model input containing top X and bottom X expressed genes with corresponding cds 
    """
    
    ###-----Part A: Load and extract the upper and lower percentile expressions######
    print('Preprocessing expression table.....................')
    df_train = pem(exprs_matrix,exprs_percentile)
    
    ###-----Part. B Load and Process CDS fasta as dict for easy look-up########## 
    print('Preprocessing fasta file with coding Sequences .....................')
    cds_dict = fasta2dict.fas2dict(CDS)
    
    
    ###-----Part C: extract the coding sequences that correspond to the IDs in expression 
    #the cds fasta expected to have more entries than the expression table  
    print('Matching expression values to coding sequences .....................')
    df_train['CDS']=[cds_dict.get(seq_ID) for seq_ID in df_train.iloc[:,0].values ] #1st column is ID column
    
    ###-----Part D: Report and drop missing entries, and warn users.
    missing= max(df_train.isna().sum())  #value for the highest number of null entries
    if missing:
        df_train.to_csv('maniso_bh_train',index=False)
        miss_IDs= list(df_train[df_train.isnull().any(axis=1)].iloc[:,0].values) #extract IDs with missing cds
        print(f'WARNING! {len(miss_IDs)} transcript IDs are missing from fasta file')
        print('Dropping missing entries for the following IDs:{}'.format("\n".join(miss_IDs)))
        df_train.dropna(axis=0, inplace=True)
    print('Final sample size for modelling= {} sequences\n\n'.format(df_train.shape[0]))
  
    #rename column names
    df_train.columns=['Seq_ID','Expression','Exprs_label', 'CDS']
    #shuffle dataset 
    if seed_num:
        df_train=shuffle(df_train, random_state=seed_num)
    else:
        df_train=shuffle(df_train)
    return df_train

if __name__=='__main__':
    prepare_training_data(exprs_matrix, CDS, exprs_percentile, seed_num)
