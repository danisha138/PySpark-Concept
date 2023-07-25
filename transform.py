transform() is used to chain the custom transformations and this function returns the new DataFrame after applying the specified transformations. This versatile function enables us to manipulate data efficiently and create new columns based on existing ones. Let's dive into a practical example to showcase its capabilities.

Real-World Example: Applying Custom Transformations

Consider a DataFrame containing information about employees, including their IDs, names, and salaries. We want to perform two custom transformations on the DataFrame:
1. Convert the "Name" column to uppercase and store the results in a new column called "New_name."
2. Increase each employee's salary by 30% and store the results in a new column called "new_sal."


from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data for DataFrame
data = [(1, "Rohit", 50000),
    (2, "Satyam", 60000),
    (3, "Danish", 70000)]

# Define the schema for the DataFrame
schema = ["Id", "Name", "Salary"]

# Create the DataFrame
df = spark.createDataFrame(data, schema)

# Define custom transformation functions
def to_upper_str_columns(df):
  return df.withColumn("New_name", upper(df.Name))

def increased_sal(df):
  return df.withColumn("new_sal", df.Salary * 1.3)

# Apply custom transformations using transform()
df_transformed = df.transform(to_upper_str_columns).transform(increased_sal)

# Show the resulting DataFrame with the new "New_name" and "new_sal" columns
df_transformed.show


#Transform and filter is always using function in pyspark. 
