#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:10:27 2017

@author: harsh
"""

import numpy as np
import pandas as pd
import re


train = pd.read_csv("en_train.csv")
test = pd.read_csv("en_test.csv")
i=0

l1=list(test["sentence_id"])
text = list(test["before"])
#print(len(l1))

l2=list(test["token_id"])
#print(l2)
l3 = []

for i in range(len(l1)):
    l3.append(str(l1[i])+"_"+str(l2[i]))
    

sub3 = pd.DataFrame({'id':l3, 'after':test.before})
sub3 = sub3[['id','after']]
sub3.to_csv('sub.csv', index=False)
#for i in test["sentence_id"].items():
#    print(str(test.sentence_id[i]))

#sub1 = pd.DataFrame({'after':test.before,'id':test.token_id})
#sub1.to_csv('sub_one.csv', index=False)








