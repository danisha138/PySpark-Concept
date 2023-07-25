#Alias Function
#The Alias function allows you to assign an alias (alternate name) to a DataFrame column. 
#This is particularly useful when dealing with complex queries or renaming columns for better readability.

##################################################################################################################
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data for DataFrame
data = [
  (1, "Soumya", 22),
  (2, "Satya", 30),
  (3, "Sangram", 25)
]

schema = ["id", "name", "age"]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Using Alias to rename the "age" column

df_with_alias = df.select(df["id"], df["name"], df["age"].alias("years_old"))

# Show the DataFrame with alias
df_with_alias.show()

In this example, we use the 'alias()' function to rename the "age" column to "years_old" in the DataFrame 'df_with_alias'. 
The DataFrame will now display the new column name "years_old" for the "age" values.
######################################################################################################################
#Cast Function
#The Cast function is used to convert a DataFrame column to a different data type. This is useful when the column needs to be in a specific format for data manipulation or analysis.

from pyspark.sql.functions import col

# Using Cast to change the data type of the "age" column
df_with_cast = df.withColumn("age", col("age").cast("string"))

# Show the DataFrame with casted column

df_with_cast.show()
