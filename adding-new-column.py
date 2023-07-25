Adding new columns to a PySpark DataFrame and performing data aggregation. 
Adding new columns allows us to enrich our data and derive additional insights, 
while aggregation techniques help us summarize and analyze data effectively. Let's dive in!

Topic 1: Adding New Columns

To add a new column to a PySpark DataFrame, we can use the 'withColumn()' function. Here's an example:

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import count, sum, avg


# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create a sample DataFrame
data = [
  (1, "Soumya", 22),
  (2, "Subham", 30),
  (3, "Rohan", 28),
  (4,"Soumya", 16),
  (5, "Subham", 40)
]

schema = ["id", "name", "age"]
df = spark.createDataFrame(data, schema)

# Add a new column to the DataFrame
new_df = df.withColumn("is_adult", expr("CASE WHEN age >= 18 THEN 'Yes' ELSE 'No' END"))
new_df.show()


In this example, we create a new column called "is_adult" based on the condition that if the age
is greater than or equal to 18, the value will be "Yes", otherwise it will be "No". The 'withColumn()' 
function returns a new DataFrame 'new_df' with the added column.

#Topic 2: Data Aggregation:

Data aggregation involves summarizing data based on specific criteria. PySpark provides various functions
for aggregation, such as 'groupBy()', 'agg()', and aggregate functions like 'count()', 'sum()', 'avg()', and more. Here's an example:

# Find count of id, sum of age, average of age on the basis of name
aggregated_df = df.groupBy("name").agg(count("id").alias("total_count"),sum("age").alias("total_age"), avg("age").alias("average_age"))
aggregated_df.show()
