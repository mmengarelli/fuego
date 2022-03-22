# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC #Evaluating Risk for Loan Approvals
# MAGIC 
# MAGIC ## Business Value
# MAGIC 
# MAGIC Being able to accurately assess the risk of a loan application can save a lender the cost of holding too many risky assets. Rather than a credit score or credit history which tracks how reliable borrowers are, we will generate a score of how profitable a loan will be compared to other loans in the past. The combination of credit scores, credit history, and profitability score will help increase the bottom line for financial institution.
# MAGIC 
# MAGIC ## The Data
# MAGIC 
# MAGIC The data used is public data from Lending Club. It includes all funded loans from 2012 to 2017. Each loan includes applicant information provided by the applicant as well as the current loan status (Current, Late, Fully Paid, etc.) and latest payment information. For a full view of the data please view the data dictionary available [here](https://resources.lendingclub.com/LCDataDictionary.xlsx).
# MAGIC 
# MAGIC <img src="https://preview.ibb.co/d3tQ4R/Screen_Shot_2018_02_02_at_11_21_51_PM.png" style="width: 350px;"/>
# MAGIC 
# MAGIC https://www.kaggle.com/wendykan/lending-club-loan-data

# COMMAND ----------

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import train_test_split

from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

import common.lending_club.functions as fn
import common.lending_club.plots as pt

fn.init()

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md #### Load Data

# COMMAND ----------

X, y = fn.load_data(spark)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

X_train_enc, X_test_enc = fn.encode_inputs(X_train, X_test)
y_train_enc, y_test_enc = fn.encode_labels(y_train, y_test)

# COMMAND ----------

# MAGIC %md #### Train
# MAGIC * MLflow Auuto-logging ✅
# MAGIC * Parameter search ✅ 

# COMMAND ----------

model = KerasClassifier(build_fn=fn.build_model, input_dim=X_train_enc.shape[1], verbose=2)

optimizers = ['rmsprop', 'adam']
inits= ['glorot_uniform', 'normal']
epochs = [1] #5, 10, 15]

param_grid = dict(optimizer=optimizers, epochs=epochs, init=inits)
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)

grid_result = grid.fit(X_train_enc, y_train_enc, use_multiprocessing=True)
best_model = grid_result.best_estimator_.model

# COMMAND ----------

# MAGIC %md #### Evaluate

# COMMAND ----------

grid_result.best_params_

# COMMAND ----------

metrics = best_model.evaluate(X_test_enc, y_test_enc)
metrics
