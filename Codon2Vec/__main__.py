# Author: Rhondene Wint (rwint@ucmerced.edu, PhD candidate@ UC Merced,California USA)
# Date of fully functional: March 2019
# Date of completion for users: July 2021
#RENAME TO __main__.py

import argparse
import os
from datetime import date
import warnings
import numpy as np

#import seaborn
#import matplotlib.pyplot as plt

if __name__=='__main__':
    about = 'About: a neural network that predicts gene expression from codon usage of coding sequences. Written by Rhondene Wint, rwint@ucmerced.edu.'
    epi_note = 'To contact the author, please make a github issue at https://github.com/rhondene/Codon2Vec/tree/main/Codon2Vec '
    parser = argparse.ArgumentParser(description=about,
                                     epilog=epi_note)
    parser.add_argument('-outfolder', help='Path of destination folder for output files', type=str, default='./C2V-{}'.format(date.today()))
    parser.add_argument('-CDS', help='Path to fasta file with species coding sequences', type=str, required=True,)
    parser.add_argument('-exprs', help='Path to expression table with gene IDs and expresion values', type=str, required=True,)
    parser.add_argument('-ep', help='Top and bottom percentile of expression for training. Default=0.1 (10th percentile)', type=float, default=0.1,)
    parser.add_argument('-maxlen', help='Maximum length of CDS (in number of codons) to retain for modelling. Default=1500 codons', type=int, default=1500, )
    parser.add_argument('-ratio', help='Ratio for spliting data into training:validation:test for model training and evaluation. Eg. 70:20:10', type=str, default='70:20:10',)
    parser.add_argument('-seed_num',help='Set a specific interger as seed to improve reproducibility of results',type=int,default=None)
    parser.add_argument('-save_prompt',help='Suppress message for save model. Options are on or off. Default is on',type=str,default='on')

    args = parser.parse_args()
    os.mkdir(args.outfolder)
    #if a seed is passed in for for reproducibility
    if args.seed_num:
        np.random.seed(args.seed_num)
        
    from mergeExprsCDS import prepare_training_data
    import nlp_preproc
    import model_build
    import model_train 
    import pandas as pd
    import tensorflow as tf 
    from keras.models import Sequential, save_model
    ###----------------------Section 1: Data Preprocessing-------------------------###
    #---->Part A: prepare training data from raw exprs and CDS files
    
    df_train=prepare_training_data(args.exprs, args.CDS,args.ep,args.seed_num)
    df_train.to_csv('processed_input.csv',index=False)
    """Checkpoint Passed!"""
    
    #----> Part B: Transform and Encode training data for NLP model input
    feature_mat, groundtruth = nlp_preproc.nlp_preproc(df_train, args.maxlen)
    print(len(feature_mat), len(groundtruth))
    """Checkpoint Passed!"""
    
    ###----------------------Section 2:  Data Modelling and Prediction------------------###
    
    #----> Part C Build Codon2vec model  
    C2V_model=model_build.model_instantiate(args.maxlen, args.seed_num)
    #print(C2V_model.summary())
    """Checkpoint Passed!"""
    
    #----> Part D : Train and evaluate model performance
    ratio = args.ratio.split(':')
    val_size=float(ratio[1])/100
    test_size= float(ratio[2])/100

    C2V_trained=model_train.model_train(C2V_model, feature_mat, groundtruth, test_size, val_size, args.outfolder, args.seed_num)
    
    
    
    # save whole trained model
    if args.save_prompt=='on':
        ans = input('Save this trained model (y/n)?')
        if ans.lower()=='y':
            save_model(C2V_trained,'{}/C2V_trained.model'.format(args.outfolder))
            print("Saved model to disk!")
    #print end message. And location of results and citation 
    
    
    
    
