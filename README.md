# Spam Detection -  Text Classification

This code classifies an email as ham or spam through training by training on Enron Emails dataset.

## Evaluation Metrics

The metrics for evaluation are listed below.

### Number of Training Files

Number of Ham Training Files: 4361
Number of Spam Training Files: 1496
Total Training Files: 4361 + 1496 = 5857

### Proababilities

Ham Probability: 0.7445791360764896
Spam Proabability: 0.2554208639235103

The formula for the calculation of probabilities is as as follows:

```
Ham Probability = (Number of Ham Training Files)/(Number of Ham Training Files + Number of Spam Training Files)
```

```
Spam Probability = (Number of Spam Training Files)/(Number of Ham Training Files + Number of Spam Training Files)
```

Log of Ham Probability: -0.29493613824701587
Log of Spam Proabability: -1.3648426475553597

The formula for the calculation of log of these probabilities is as as follows:

```
Log of Ham Probability = log((Number of Ham Training Files)/(Number of Ham Training Files + Number of Spam Training Files))
```

```
Log of Spam Probability = log((Number of Spam Training Files)/(Number of Ham Training Files + Number of Spam Training Files))
```

### Confusion Matrix

True Positive: 1443
True Negative: 3436
False Positive: 236
False Negative: 57

### Accuracy

0.9433488012374324

```
Accuracy = (TP + TN)/(TP + TN + FP + FN)
```

### Precision

0.8594401429422275

```
Precision = TP/(TP + FP)
```

### Recall

0.962 

```
Recall = TP / (TP + FN)
```

### F1 Score

0.9078326517772884

```
F1 Score = (2 * Precision * Recall)/(Precision + Recall)
```
