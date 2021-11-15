# -*- coding: utf-8 -*-
"""
Module to train and evaluate C2V

@author: RWint
"""
import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import eval_plots #custom module that computes model valuation metrics and related plots

from sklearn.model_selection import train_test_split as tts


from pandas.core.common import SettingWithCopyWarning
import warnings

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

seaborn.set_context('poster')

##Reproducibility
from tensorflow import set_random_seed


def model_train(C2V_model, feature_mat,groundtruth, test_size, val_size, out_folder,seed_num):
    """Input
    model: instantiated and compiled keras neural network model object 
    feature_mat: preprocessed input matrix (2-D numpy array)
    ground_truth: 1-D array of expression labels for each input sequence
    test_size: decimal fraction of input that should be allocated as hold-out test set
    val_size: decimal fraction of input that should be allocated as hold-out validation set
    Outputs:
        trained model
    """
    ## if user passed in a seed number
    if seed_num:
        np.random.seed(seed_num)
        set_random_seed(seed_num)
    
    #first split test set
    X_train,X_test,  y_train, y_test= tts(feature_mat,groundtruth,test_size=test_size)
    #save the training and test sets
    
    
    #fit and train model
    train_history = C2V_model.fit(X_train, y_train, validation_split=val_size, epochs=10, batch_size=32, verbose=0)
    loss,accuracy = C2V_model.evaluate(X_test,y_test,verbose=1)
    print('Classification accuracy on test set=', (accuracy*100),'%')
     
    #plot training diagnosis
    print('Generating Train-Validation loss plot')
    eval_plots.train_plot(train_history, out_folder)
    #plot evaluation on test set
    print('Generating Confusion Matrix plot ............')
    performance_dict=eval_plots.plot_confmat_AUC(X_test, y_test, C2V_model, out_folder)
    
   
    print(performance_dict)
    
    #write performance to file 
    print('Saving evalution of model performance to file........')
    with open('{}/model_evaluation.txt'.format(out_folder),'w') as output:
        for metric,value in performance_dict.items():
            output.write("{}\t{}\n".format(metric,value))
    print('Save Completed!')  
     
    return C2V_model
    
    
 
