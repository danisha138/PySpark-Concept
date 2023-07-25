Data manipulation techniques in PySpark DataFrames: data filtering and sorting

Both filtering and sorting are crucial for extracting relevant information and
organizing data for effective analysis. Let's dive into practical examples to understand these concepts in PySpark.

Example 1:
Filter out the records of adults whose age is greater than or equal to 18.

---------------------------------------------------
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data for the DataFrame
data = [
  (1, "Soumya", 23),
  (2, "Satya", 30),
  (3, "Rohit", 17),
  (4, "Sangram", 21),
  (5, "Sunil", 16)
]

schema = ["id", "name", "age"]

# Create the DataFrame
df = spark.createDataFrame(data, schema)

# Filter out records of adults (age >= 18)
adult_df = df.filter(df.age >= 18)

# Show the filtered DataFrame
adult_df.show()
-----------------------------------------------------------

In this example, we use the 'filter()' function to extract the records of adults 
whose age is greater than or equal to 18. The resulting DataFrame 'adult_df' will only contain the rows of Soumya, Satya and Sangram.

Example 2: Sorting Data by Age in Descending Order
Continuing with the same DataFrame 'df', let's sort the data by age in descending order
to get the records of adults in descending age order.

---------------------------------------------------
# Sort the DataFrame by age in descending order
sorted_df = df.sort("age", ascending=False)

# Show the sorted DataFrame
sorted_df.show()
