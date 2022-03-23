# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag

# COMMAND ----------

class MyTestFixture(NutterFixture):
   def run_test_loan_risk_tf(self):
      dbutils.notebook.run("/Repos/michael.mengarelli@databricks.com/fuego/notebooks/loan_risk_tf", 600)

   def assertion_test_loan_risk_tf(self):
      assert (1 == 1)

# COMMAND ----------

result = MyTestFixture().execute_tests()
print(result.to_string())
