# Data preparation

## Structuring your experiment data ##

Always divide your data into the following blocks:

* Split your data into a _training set_ and a _test set_
* Split the training set further into _training set_ and a _validation_ set

When evaluating the correctness of your results, always validate with the **validation** set. Do not use the test set until you think your model is ready for prime time.

## Considerations for splitting data

### Random shuffling

If you have a data set ordered in classes, ensure you do random shuffling. I.e: if you have a dataset representing single digits (classes 0-9) and you split your data 80/20 without random shuffling, your training set will not have instances of classes 8-9.

### Time series

Do not do random shuffling if you have time series data. Otherwise, the progression of time will be lost

### Data redundancy

Remove data dups. If you shuffle your data and it das dups, these dups might end up in both the test, validation and training sets.

## K-fold Cross-validation

If your data set is too small, splitting the data set might cause your sets to loose statistical significance. In this case, use the K-fold approach to split the data into _x_ folds, each of which will be evaluated individually and the result of those runs averaged to produce a more solid result.