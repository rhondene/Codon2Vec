# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:20:02 2021
Module for computing evaluation metrics and generating plots
@author: RWint
"""
import numpy as np
import sklearn.metrics
import seaborn
import matplotlib.pyplot as plt


seaborn.set_context('poster')


""" Plot model convergence on train validation set """
def train_plot(history, out_folder):
    """plots loss curves for training and validation set
    Can be used to diagnose overfitting or underfitting (bias-variance trade-off)
    """
    title='Codon2Vec Prediction Accuracy on Training vs Validation Sets'
    plt.figure(figsize=(10,8))
    plt.plot(history.history['accuracy'], linewidth=4)
    plt.plot(history.history['val_accuracy'], linewidth=4)
    plt.title(title,
              fontsize=16, fontweight='bold')
    plt.ylabel('Prediction Accuracy', fontsize=16)
    plt.xlabel('Epoch', fontsize=16)
    plt.xticks(fontsize=16); plt.yticks(fontsize=16)
    plt.legend(['Training set', 'Validation set'], loc='upper left', fontsize=22)
    #LEARN HOW TO CALL varibales from main into this module
    plt.savefig('{}/model_diagnosis_plot.png'.format(out_folder), dpi=300, bbox_inches='tight')
    return 
    """ Model evalution"""
    
def plot_confmat_AUC(X_test, y_test, model, out_folder):
    
    """ Evaluates and plots the performance of trained model on hold-out test set. 
    Model evaluation metrics include Accuracy, AUC-ROC, Sensitivity, Specificity, Precision"""
    predictions=(model.predict(X_test))
    y_pred = predictions
    ##binarise sigmoid activation probs 
    predictions[predictions >= 0.5] =1
    predictions[predictions <0.5]=0

    ##-----plot confusion matrix
    
    
    confmat = sklearn.metrics.confusion_matrix(y_true=y_test, y_pred =y_pred) 
 
    fig,ax = plt.subplots(figsize=(5, 5))
    ax.matshow(confmat, cmap= plt.cm.Blues, alpha=0.3)
    for i in range(confmat.shape[0]):
        for j in range(confmat.shape[1]):
            ax.text(x=j, y=i,
                    s= confmat[i,j],
                   va = 'center', ha='center', fontsize=18)
    plt.xlabel('Predicted Exprs Level',labelpad=10)
    plt.ylabel('True Exprs Level',labelpad=10)
    plt.savefig('{}/model_confusion_matrix.png'.format(out_folder), dpi=300, bbox_inches='tight')
    print('Confusion matrix saved!')
    
    #### plot AUC-ROC curve
    TP = confmat[1, 1]
    TN = confmat[0, 0]
    FP = confmat[0, 1]
    FN = confmat[1, 0]
    
    
  

    """ Model performance metrics stats"""
    class_error = (FP + FN) / float(TP + TN + FP + FN)
    sensitivity = TP / float(FN + TP)
    specificity = TN / (TN + FP)
    precision = TP / float(TP + FP)
    
    
       
    y_pred = model.predict_proba(X_test)
    pct_auc = sklearn.metrics.roc_auc_score(y_test, y_pred) * 100
    fpr, tpr, _ = sklearn.metrics.roc_curve(y_test, y_pred)
    roc_auc = sklearn.metrics.auc(fpr, tpr)
    
    ####-----------> AUC-ROC Plot
    print('Generating AUC-ROC Plot ............')
    plt.figure(dpi=300)
    lw = 2
    plt.plot(fpr, tpr, color='maroon',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='mediumblue', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate\n(1 - Specificity)', fontsize=14, fontweight='bold')
    plt.ylabel('True Positive Rate\n(Sensitivity)',  fontsize=14, fontweight='bold')
    plt.xticks(fontsize=14);plt.yticks(fontsize=14)
    #plt.title('AUC-ROC for Neural Network Predicting Expression based coding sequence in {}'.format(sp),fontsize=14, fontweight='bold')
    plt.legend(loc="upper left", fontsize=16,bbox_to_anchor=(0, 1.17), ncol=1)
    plt.text(0.4, 0.03, 'Misclassification Error:{:.2f} \n Sensitivity(Recall): {:.2f}\n Precision: {:.2f} \n Specificity: {:.2f}'.format(class_error,sensitivity,precision,specificity), 
             style='italic',
        bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 3},fontsize=14)
   
    plt.savefig('{}/auc_roc.png'.format(out_folder), bbox_inches='tight',dpi=300)
   
    print('AUC-ROC plot saved!')

   ## return metrics Missclass error, AUC score, sensitivity , specificity
    performance_dict={'Aucuracy':1-class_error, 'AUC-ROC':roc_auc,
                'Sensitivity':sensitivity,'Specificity': specificity,
                'Precision': precision}
    return performance_dict




