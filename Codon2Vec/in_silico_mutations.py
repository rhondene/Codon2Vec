# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:49:34 2021

@author: RWint
"""

codon_sequence=[]  #stores the order codons of a cds

for cod range(0,len(cds),3):
    cod=cds[c:c+3]
    
    #check if cod is optimal
    if cod in species_pref_codon_list:
        #recode with non_pref
        cod=non_pref_mapping[cod]
        
    codon_sequence.append(cod)
#for a given species, stores the synonymous pref:non_pref mapping

non_pref_mapping[]