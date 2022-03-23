import os

def get_user_id(dbutils):
  return dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().apply('user')

def get_dbfs_home(dbutils):
  return os.path.join("/home/", get_user_id(dbutils))

def get_user_home(dbutils):
  return os.path.join("/dbfs/home", get_user_id(dbutils))