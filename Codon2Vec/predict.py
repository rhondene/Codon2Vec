# -*- coding: utf-8 -*-
"""
@author: RWint
Loads the pre-trained model and run predictions on new sequences
"""

import argparse
import os
import pandas as pd
import fix_fasta
from keras.models import Sequential, save_model, load_model

from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  #Suppress UserWarning printouts



##write preprocessing function  for input sequence
def preproc_seq(IDs,CDS):
    """
    Transforms CDS to space-delimited string of codons
    Input:
        list of sequences
    Outputs:
        list of sequences as space-delimited codons"""
    codons = []
    final_ids=[]
    for i in range(len(CDS)):
            seq = CDS[i]
            ID= IDs[i]
            if len(seq)%3 !=0:  ## only CDS that are exact multiple of 3
                print(f'{IDs[i]} CDS is not multiple of 3....Skipping Sequence')
                continue
            cod_list = []
            for j in range(0, len(seq),3):
                codon = seq[j:j+3]
                cod_list.append(codon)
              
            cods = " ".join(cod_list)
            final_ids.append(ID)
            codons.append(cods)
    return (codons,final_ids)


def encode_features(cod_list,max_len=1500):
    """ Input:
        codons: list of sequences each formatted as a string of space-separated codons
    returns the encoded and padded feature matrix"""

    vocab_size=64
    encoded_codons = [one_hot(seq,vocab_size) for seq in cod_list]
    
    ##Step2. Padding/trimming
    padded_codons = pad_sequences(encoded_codons,maxlen= max_len, padding='post')
   
    return padded_codons
    
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('-model_j', help='Path of json file of trained model', type=str, required=True, metavar='')
    parser.add_argument('-model', help='Path of saved trained model', type=str, required=True)
    parser.add_argument('-fasta', help='Path of fasta formatted file with coding sequence(s)', type=str, required=True)
    parser.add_argument('-out', help='Path of output text file with predictions of each sequence', type=str, required=True)
    args= parser.parse_args()
    
    IDs,CDS = fix_fasta.fix_fasta(args.fasta)  #returns headers and sequences but only want sequences
    #####----------------preprocess the sequences for model input
    #transforms each coding sequence into a list of space separated codons
    cod_list,final_ids = preproc_seq(IDs,CDS)
    pred_df=pd.DataFrame([final_ids]).T
    pred_df.columns=['SeqID']
    #encode the codons in similar manner as training data
    encoded_seqs = encode_features(cod_list,max_len=1500)
    
    #####------------------Load the trained model------
    C2V_trained = load_model(args.model,custom_objects=None, compile=True)
    #####------------------Perform predictions-------------
    
    preds = C2V_trained.predict(encoded_seqs)
    pred_df['Prediction_prob']=preds.flatten()
        
    ##write predictions and ID to file:
    pred_df.to_csv('{}_predictions.tsv'.format(args.out), sep='\t')

    
    
   
       
   
    
