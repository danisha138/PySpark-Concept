Reshaping allows us to transform the structure of data, while modifications enable us to update or create new columns based on existing data. 
Let's dive into practical examples to understand how to reshape and modify DataFrames in PySpark.

Example : Pivoting Data

Assuming we have a PySpark DataFrame called 'df' with columns "name", "category", and "value", representing data as follows:

-----------------------------------------------------------------------------
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data for the DataFrame
data = [
  ("Soumya", "A", 10),
  ("Soumya", "B", 15),
  ("Satya", "A", 20),
  ("Satya", "B", 25)
]

schema = ["name", "category", "value"]

# Create the DataFrame
df = spark.createDataFrame(data, schema)

# Pivot the DataFrame to reshape data
pivoted_df = df.groupBy("name").pivot("category").sum("value")

# Show the pivoted DataFrame
pivoted_df.show()
