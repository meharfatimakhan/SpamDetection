# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:10:14 2020

@author: Dell
"""
import time
start_time = time.time()
import os
from collections import Counter, defaultdict
import operator
import string
import math
import re
from stop_words import get_stop_words


####################################### TRAINING ###########################################
stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

hamFiles = os.listdir("C:\\Users\\pak\\Downloads\\IR\\train\\ham")
lenHam = len(hamFiles)
print("Number of Ham Files: ",lenHam)

spamFiles = os.listdir("C:\\Users\\pak\\Downloads\\IR\\train\\spam")
lenSpam = len(spamFiles)
print("Number of Spam Files: ",lenSpam)

hamProbability = (lenHam) / (lenSpam + lenHam)
print("Ham Probability: ",hamProbability)

spamProbability = (lenSpam) / (lenSpam + lenHam)
print("Spam Probability: ",spamProbability)

logPriorHam = math.log(hamProbability)
print("Log of Ham Probability: ",logPriorHam)

logPriorSpam = math.log(spamProbability)
print("Log of Spam Probability: ",logPriorSpam)
    
training_data = set()
ham_list = []
hamWordCount = 0
trainHam = {}
for directories, subdirs, files in os.walk("C:\\Users\\pak\\Downloads\\IR\\train\\"):
    if (os.path.split(directories)[1]  == 'ham'):
        for filename in files:     
            with open(os.path.join(directories, filename),errors='ignore') as f:
                data = f.read()
                data = data.lower()
                data = re.sub(r'[^a-z]', ' ', data)
                data = data.split()
                n_data = []
                for word in data:
                    if word not in stop_words:
                        n_data.append(word)        
                training_data.update(n_data)
                for word in n_data:
                    hamWordCount = hamWordCount + 1
                    ham_list.append(word)
hamCounter = Counter(ham_list)

spam_list = []
trainSpam = {}
spamWordCount = 0
for directories, subdirs, files in os.walk("C:\\Users\\pak\\Downloads\\IR\\train\\"):
    if (os.path.split(directories)[1]  == 'spam'):
        for filename in files:      
            with open(os.path.join(directories, filename),errors='ignore') as f:
                data = f.read()
                data = data.lower()
                data = re.sub(r'[^a-z]', ' ', data)
                data = data.split()
                n_data = []
                for word in data:
                    if word not in stop_words:
                        n_data.append(word)        
                training_data.update(n_data)
                for word in n_data:
                    spamWordCount = spamWordCount + 1
                    spam_list.append(word)
spamCounter = Counter(spam_list)
                
vocabCount = len(training_data)

hamLogLikelihood = {}
for word,occurances in hamCounter.items():
        hamLogLikelihood[word] = math.log((occurances + 1)/(vocabCount + hamWordCount))
    
spamLogLikelihood = {}
for word,occurances in spamCounter.items():
        spamLogLikelihood[word] = math.log((occurances + 1)/(vocabCount + spamWordCount))

####################################### TESTING ###########################################
        
TP = 0
TN = 0
FP = 0
FN = 0
for directories, subdirs, files in os.walk("C:\\Users\\pak\\Downloads\\IR\\test\\"):
    if (os.path.split(directories)[1]  == 'ham'):
        for filename in files:      
            with open(os.path.join(directories, filename),errors='ignore') as f:
                data = f.read()
                data = data.lower()
                data = re.sub(r'[^a-z]', ' ', data)
                data = data.split()
                n_data = []
                for word in data:
                    if word not in stop_words:
                        n_data.append(word)  
                temp1 = logPriorHam
                temp2 = logPriorSpam
                for word in n_data:
                    if word in hamLogLikelihood.keys():
                        temp1 = temp1 + hamLogLikelihood[word]
                    else:
                        temp1 = temp1 + (math.log(1/(vocabCount + hamWordCount)))
                        
                    if word in spamLogLikelihood.keys(): 
                        temp2 = temp2 + spamLogLikelihood[word]
                    else:
                        temp2 = temp2 + (math.log(1/(vocabCount + spamWordCount)))
                        
                if (temp2 < temp1):
                    TN = TN + 1    
                else:
                    FP = FP + 1
                    
for directories, subdirs, files in os.walk("C:\\Users\\pak\\Downloads\\IR\\test\\"):
    if (os.path.split(directories)[1]  == 'spam'):
        for filename in files:      
            with open(os.path.join(directories, filename), errors = 'ignore') as f:
                data = f.read()
                data = data.lower()
                data = re.sub(r'[^a-z]', ' ', data)
                data = data.split()
                n_data = []
                for word in data:
                    if word not in stop_words:
                        n_data.append(word)  
                temp1 = logPriorHam
                temp2 = logPriorSpam
                for word in n_data:
                    if word in hamLogLikelihood.keys():
                        temp1 = temp1 + hamLogLikelihood[word]
                    else:
                        temp1 = temp1 + (math.log(1/(vocabCount + hamWordCount)))
                        
                    if word in spamLogLikelihood.keys(): 
                        temp2 = temp2 + spamLogLikelihood[word]
                    else:
                        temp2 = temp2 + (math.log(1/(vocabCount + spamWordCount)))
                        
                if (temp2 <= temp1):
                    FN = FN + 1
                else:
                    TP = TP + 1
                

print("True Positive: ", TP)
print("True Negative: ",TN)
print("False Positive: ",FP)
print("False Negative: ",FN)
precision = TP/(TP + FP)
print("Precision: ",precision)
accuracy = (TP + TN)/(TP + TN + FP + FN)
print("Accuracy: ",accuracy)
recall = TP / (TP + FN)
print("Recall: ",recall)
F1 = (2 * precision * recall)/(precision + recall)
print("F1 Score: ",F1)
print("--- %s seconds ---" % (time.time() - start_time))