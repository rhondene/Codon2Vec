# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:00:05 2021
Codon2vec Model specification 
@author: RWint
"""
##deep learning training  libraries
import numpy as np

def model_instantiate(max_len,seed=None):
   ## set seed before loading keras for reproducibility

   if seed:
       np.random.seed(seed)
       
   from keras.models import Sequential, Model
   from keras.layers import Dense, Embedding,Flatten, Input, BatchNormalization, Dropout
   from keras.optimizers import Adam
   from keras.utils import to_categorical
    
   C2V_model = Sequential()
   #each of the 64 uniqe codon (feature vocabulary) is transformed into 4-dim dense vector
   embed_layer=Embedding(input_dim=64,output_dim=4, input_length=max_len)
   
   C2V_model.add(embed_layer)
   C2V_model.add(Dropout(0.4))
   C2V_model.add(Flatten())   #unroll 3d tensor into 1-d 
   C2V_model.add(Dense(4,activation='relu'))  ##
   C2V_model.add(Dropout(0.2))
   C2V_model.add(Dense(1,activation='sigmoid'))  ##output layer is only one layer because either high or low
    
   #compile theC2V_model
   C2V_model.compile(optimizer=Adam(lr=0.005, beta_1=0.9, beta_2=0.999, decay=0.01),
                           metrics=['accuracy'], loss='binary_crossentropy')
   return C2V_model

