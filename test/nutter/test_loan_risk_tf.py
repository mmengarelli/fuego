# Databricks notebook source
from testbase import BaseFixture

class MyTestFixture(BaseFixture):
   def run_test_loan_risk_tf(self):
      dbutils.notebook.run("/Repos/michael.mengarelli@databricks.com/fuego/notebooks/loan_risk_tf", 600)

   def assertion_test_loan_risk_tf(self):
      assert (1 == 1)

# COMMAND ----------

result = MyTestFixture().execute_tests()
print(result.to_string())
