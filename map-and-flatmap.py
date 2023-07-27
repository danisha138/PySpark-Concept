#Map Function:

The map function is used to apply a specified function to each element of an RDD or DataFrame and
returns a new RDD with the transformed results. It takes one input and produces one output for each element, maintaining the original RDD's size.

Here's an example of using 'map' to increase the salaries of employees by 10%:


from pyspark.sql import SparkSession
# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

data = [(1, "Alice", 50000),
    (2, "Rohan", 60000),
    (3, "Hiren", 70000),
    (4, "Salman", 40000)]

# Create an RDD
rdd = spark.sparkContext.parallelize(data)

def increase_salary(row):
  id, name, salary = row
  increased_salary = salary * 1.1
  return (id, name, int(increased_salary))

# Apply the map function to increase the salary of each employee
mapped_rdd = rdd.map(increase_salary)
mapped_rdd.collect()  

##Output
[(1, 'Alice', 55000),
 (2, 'Rohan', 66000),
 (3, 'Hiren', 77000),
 (4, 'Salman', 44000)]

# Convert the RDD back to a DataFrame
schema = ["Id", "Name", "Salary"]
df_with_increased_salary = spark.createDataFrame(mapped_rdd, schema)

df_with_increased_salary.display()


flattened_rdd = rdd.flatMap(lambda row: [row, row])
flattened_rdd.collect()
df_duplicated = spark.createDataFrame(flattened_rdd, schema)
df_duplicated.show()



------------------------------------------------
#The 'flatMap' function is similar to 'map',but it allows returning multiple elements for each input element. 
It flattens the results into a single output RDD or DataFrame. 
The returned Dataset will return more rows than the current DataFrame. It is also referred to as a one-to-many transformation function. 
This is one of the major differences between flatMap() and map().

let's use 'flatMap' to make each row as duplicate.

flattened_rdd = rdd.flatMap(lambda row: [row, row])
df_duplicated = spark.createDataFrame(flattened_rdd, schema)
df_duplicated.show()
