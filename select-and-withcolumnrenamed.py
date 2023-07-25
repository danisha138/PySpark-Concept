#Selecting Specific Columns

To select specific columns from a PySpark DataFrame, you can use the `select()` function and pass the column names as arguments. Here's an example:

-----------------------------------------------------------
# Select specific columns from the DataFrame
selected_df = df.select("column1", "column2", "column3")
selected_df.show()
-----------------------------------------------------------

Replace "column1", "column2", and "column3" with the names of the columns you want to select. The 'select()' function returns a new DataFrame with only the specified columns.

#Renaming Columns

To rename specific columns in a PySpark DataFrame, you can use the 'withColumnRenamed()' function. Here's an example:

-------------------------------------------------------------
# Rename a specific column in the DataFrame
renamed_df = df.withColumnRenamed("old_column", "new_column")
renamed_df.show()
