# -*- coding: utf-8 -*-
"""
Module to preprocess and transform training data for NLP model 
Created on Fri Jul 23 16:02:36 2021
@author: RWint
"""
import numpy as np   
import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import warnings

from keras.preprocessing.text import one_hot
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.simplefilter(action="ignore", category=UserWarning)


###----->Part A:  
def preproc_features_labels(df_train):
    """Input:
        df_training: dataframe of expression and coding sequences
    Output:
        codons: list of each sequence as a string of space-separated codons
        labels: list of expression level of cds High or Low
        """
    codons = []
    labels = []
    for i in range(len(df_train['CDS'].values)):
            seq = df_train['CDS'].values[i]
            if len(seq)%3 !=0:  ## only CDS that are exact multiple of 3
                print('{} CDS is not multiple of 3....Skipping pair'.format(df_train['Seq_ID'].values[i]) )
                continue
            cod_list = []
            for j in range(0, len(seq),3):
                codon = seq[j:j+3]
                cod_list.append(codon)
              
            cods = " ".join(cod_list)   #Represent CDS a space-delimited string of codons
            codons.append(cods)
            labels.append(df_train['Exprs_label'].values[i])
    return codons,labels

###--->PartB. Padding of codons AND categorical encoding of labels 

def encode_features_labels(codons,labels,max_len):
    """ Input:
        codons: list of sequences each formatted as a string of space-separated codons
        labels: list of Expression level (High or Low) for each sequence in codons list 
    returns the encoded and padded feature matrix, and re-coded target labels """

    vocab_size=64
    encoded_codons = [one_hot(seq,vocab_size) for seq in codons]
    
    ##Step2. Padding/trimming
    #keras embedding layer requires individual sequences to be same length
    padded_codons = pad_sequences(encoded_codons,maxlen= max_len, padding='post')
    
    ##one hot encode expression labels
    target = []
    for exprs in labels:
        if exprs == 'Low':
            target.append(0)
        if exprs == 'High':
            target.append(1)
    target = np.asarray(target)
    print('label shape={} before categorical encoding'.format(target.shape))
    target= np.squeeze(np.asarray(target))
    target = target.reshape(target.shape[0],1)
    print('label shape={} after categorical encoding'.format(target.shape))

    return padded_codons, target  

# linker function to the transformation functions
def nlp_preproc(df_train,max_len=1500):
    #call the processing functions
    codons,labels=preproc_features_labels(df_train)
    
    return encode_features_labels(codons,labels,max_len)
    