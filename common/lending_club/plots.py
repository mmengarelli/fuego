import matplotlib.pyplot as plt

def plot_accuracy(history):
  plt.plot(history['accuracy'])
  plt.title('Accuracy per Epoch')
  plt.ylabel('Accuracy')
  plt.xlabel('Epoch')
  plt.legend(['train'], loc='upper left')
  
  fig = plt.figure(1)
  fig_loc = "accuracy.png"
  
  fig.savefig(fig_loc)
  return fig_loc

def plot_loss(history):
  plt.plot(history['loss'])
  plt.title('Loss per Eopch')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(['train'], loc='upper left')
  
  fig = plt.figure(1)
  fig_loc = "loss.png"

  fig.savefig(fig_loc)
  return fig_loc
