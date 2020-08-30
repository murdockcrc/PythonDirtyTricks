*Notes from Deep learning with Python. Chollet. 2018*

# Define the problem and assemble the dataset

* What will your input data be? What are you trying to predict?
* Define the problem type:
    * Binary classification
    * Multiclass classification
    * Scalar regression
    * Vector regression
    * Multiclass, multilabel classification
    * Clustering
    * Generation
    * Reinforcement

# Choose a measure of success

Your metric of success will guide the choice of a loss function

# Decide on an evaluation protocol

* Maintaining a hold-out validation set
* K-fold cross-validation - when the dataset is small
* Iterated K-fold validation - for highly-accurate model evaluation when the dataset is small

# Prepare your data

* Data must be expressed as tensors
* Normalize the values of the features, such as [-1, 1] or [0, 1]
* Decide if it is worth to do some feature engineering

# Developing a model that is better than the baseline

A baseline is basically a random prediction.

Build your first working model:

* Last-layer activation
* Loss function
* Optimization configuration

Use the following table for guidance:

|Problem type|Last-layer activation|Loss function|
|---|---|---|
|Binary classification|sigmoid|binary_crossentropy|
|Multicass, single label classification|softmax|categorical_crossentropy|
|Multiclass, multilabel classification|sigmoid|binary_crossentropy|
|Regression to arbitrary values|None|mse|
|Regression to values between 0 and 1|sigmoid|mse or binary_crossentropy|