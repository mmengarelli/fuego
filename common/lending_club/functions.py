import warnings

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

import tensorflow as tf
from tensorflow.keras import layers, regularizers, metrics
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.metrics import AUC, Precision, Recall

def init():
  warnings.filterwarnings("ignore")  
  print("TF Version:", tf.__version__, "GPUs:", tf.config.list_physical_devices('GPU'))
  print("Keras Version:", tf.keras.__version__)

def load_data(spark):
  df = spark.table("mikem.loanstats_all").fillna(0).toPandas()
  X = df.loc[:, df.columns != 'bad_loan']
  y = df['bad_loan']
  return X, y

def encode_inputs(X_train, X_test):
  ohe = OneHotEncoder(handle_unknown='ignore')
  ohe.fit(X_train)
  X_train_enc = ohe.transform(X_train)
  X_test_enc = ohe.transform(X_test)
  
  return X_train_enc, X_test_enc

def encode_labels(y_train, y_test): 
  le = LabelEncoder()
  le.fit(y_train)
  y_train_enc = le.transform(y_train)
  y_test_enc = le.transform(y_test)
  
  return y_train_enc, y_test_enc

def build_model(input_dim,optimizer='rmsprop', init='glorot_uniform'):
  model = Sequential()
  model.add(Dense(17, 
                  kernel_initializer=init, 
                  input_dim=input_dim,
                  kernel_regularizer=regularizers.l2(1e-2), 
                  activation='relu'))
  #model.add(Dropout(0.2))  
  model.add(Dense(1, activation='sigmoid'))
  
  model.compile(optimizer=optimizer,
                loss='binary_crossentropy',
                metrics=['accuracy'])
  
  return model
