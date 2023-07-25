Reading different file formats in PySpark. Assume we have the files named as "demo" in different format like csv, json, parquet and avro.

Syntax to read different format of data:

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Read CSV file
df_csv = spark.read.csv('demo.csv', header=True, inferSchema=True)

# Read JSON file
df_json = spark.read.json('demo.json')

# Read Parquet file
df_parquet = spark.read.parquet('demo.parquet')

# Read Avro file
df_avro = spark.read.format('avro').load('demo.avro')


File Reading Summary:

- For CSV files, use "spark.read.csv()" and specify options like header and schema inference to read the data into a DataFrame.
- For JSON files, use "spark.read.json()" to read the data into a DataFrame. JSON files can have a nested structure, making them ideal for complex data.
- For Parquet files, use "spark.read.parquet()" to efficiently read columnar data stored in the Parquet format.
- For Avro files, use "spark.read.format('avro').load()" to read the data into a DataFrame
