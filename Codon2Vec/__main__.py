# Author: Rhondene Wint (rwint@ucmerced.edu, PhD candidate@ UC Merced,California USA)
# Date of fully functional: March 2019
# Date of completion for users: July 2021
#RENAME TO __main__.py

import argparse
import os
from datetime import date
import warnings
from tensorflow import set_random_seed
from keras.models import Sequential, save_model
#import seaborn
#import matplotlib.pyplot as plt




#model performance evaluation
"""
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
"""


##### Part A: Prepare training data from expression and coding sequences



#def preprocess_training_data(df_train, split_ratio)


if __name__=='__main__':
    about = 'one sentence about codon2vec does. Author and date and citation '
    epi_note = 'link to my github to report issues '
    parser = argparse.ArgumentParser(description=about,
                                     epilog=epi_note)
    parser.add_argument('-outfolder', help='Path of destination folder for output files', type=str, default='./C2V-{}'.format(date.today()), metavar='')
    parser.add_argument('-CDS', help='Path to fasta file with species coding sequences', type=str, required=True, metavar='')
    parser.add_argument('-exprs', help='Path to expression table with gene IDs and expresion values', type=str, required=True, metavar='')
    parser.add_argument('-ep', help='Expression percentile to train frame.That is the top and bottom X percentile of expressed genes. Default = 0.1 (10 percentile)', type=float, default=0.1, metavar='')
    parser.add_argument('-maxlen', help='Maximum length of CDS (in number of codons) to retain for modelling. Default=1500 codons', type=int, default=1500, metavar='')
    parser.add_argument('-ratio', help='Ratio for spliting data into training:validation:test for model training and evaluation. Eg. 70:20:10', type=str, default='70:20:10', metavar='')
    #parser.add_argument('save_train_data', help='To save the combined expression and CDS table after laoding and preprocessing: Enter True or False', type=bool, default=True)
    parser.add_argument('-seed_num', help='Set a specific interger as seed to minimize randomness of results', type=float, default=None,metavar='')
    ### add optional arguments etc 
    #os.mkdir(args.output)
    args = parser.parse_args()
    os.mkdir(args.outfolder)
    
    from mergeExprsCDS import prepare_training_data
    import nlp_preproc
    import model_build
    import model_train 
    import pandas as pd
    import numpy as np

    #if a seed is passed in for for reproducibility
    if args.seed_num:
        set_random_seed(args.seed_num)
        np.random.seed(args.seed_num)   

 
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
    C2V_model=model_build.model_instantiate(args.maxlen)
    #print(C2V_model.summary())
    """Checkpoint Passed!"""
    #----> Part D : Train and evaluate model performance
 
    ratio = args.ratio.split(':')
    val_size=float(ratio[1])/100
    test_size= float(ratio[2])/100
   
    
    C2V_trained=model_train.model_train(C2V_model, feature_mat, groundtruth, test_size, val_size, args.outfolder, args.seed_num)
    
    
    ## print output message and write results of performance dict to /t file#
    # save whole trained model
    
    ans = input('Save this trained model (y/n)?')
    if ans.lower()=='y':
        save_model(C2V_trained,f'{args.outfolder}/C2V_trained.model')
        print("Saved model to disk!")
    #print end message. And location of results and citation 
    
    
    
    
