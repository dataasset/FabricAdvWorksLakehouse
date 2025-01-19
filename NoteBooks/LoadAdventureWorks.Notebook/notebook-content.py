# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2608b966-fc63-4cf7-a9b7-12af8fde3ce6",
# META       "default_lakehouse_name": "lakehouse_advworks",
# META       "default_lakehouse_workspace_id": "d43fbdc1-e2d2-49cf-a10c-69a92c8209ed"
# META     }
# META   }
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimAccount.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimAccount")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimCurrency.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimCurrency")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimCustomer.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimCustomer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimCustomer.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimCustomer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimDate.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimDate")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimDepartmentGroup.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimDepartmentGroup")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimEmployee.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimEmployee")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimGeography.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimGeography")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimOrganization.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimOrganization")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimProduct.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimProduct")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimProductCategory.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimProductCategory")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimProductSubcategory.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimProductSubcategory")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimPromotion.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimPromotion")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#V order thing you can ignore those two lines
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimReseller.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimReseller")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimSalesReason.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimSalesReason")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/DimSalesTerritory.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimSalesTerritory")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/DimScenario.csv")
df.write.mode("overwrite").format("delta").save("Tables/DimScenario")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").option("delimiter","|").format("csv").load("Files/AdventureWorks/FactCallCenter.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactCallCenter")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactCurrencyRate.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactCurrencyRate")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactFinance.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactFinance")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactInternetSales.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactInternetSales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactProductInventory.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactProductInventory")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactResellerSales.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactResellerSales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactSalesQuota.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactSalesQuota")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Thanks to MIM for help with this code
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
#Load from the default lakehouse, make sure you click on the pin <=============
from pyspark.sql.types import *
df = spark.read.option("header", "true").format("csv").load("Files/AdventureWorks/FactSurveyResponse.csv")
df.write.mode("overwrite").format("delta").save("Tables/FactSurveyResponse")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
