Topic 1: Dropping Null Values

----------------------------------------------------
🎯 Drop rows with any null values
df_without_nulls = df.dropna(how="any")

🎯 Drop rows with all null values
df_without_all_nulls = df.dropna(how='all')


🎯 Drop rows from dataframe of any particular columns contains null value
df_without_null_columns = df.dropna(subset='column_name')

-----------------------------------------------------

Topic 2: Filling Null Values

🎯 Techniques to fill null values with meaningful or default values using the 'fillna()' function.

----------------------------------------------------

🎯 Replace 0 for null for all integer columns
df.na.fill(value=0).show()

🎯 Replace 0 for null on only a particular column 
df.na.fill(value=0,subset=["column_name"]).show()

🎯 Replace NULL/None values with an empty string
df.na.fill("").show()

###################################################################################
#Identify rows with null values
null_rows = df.filter(df.column_name.isNull())
null_rows.show()

#Identify rows without null values
non_null_rows = df.filter(df.column_name.isNotNull())
non_null_rows.show()


#Replace the "column_name" with your particular column name.

----------------------------------------------
# Find count for empty, None, Null, Nan with string literals.

df2 = df.select([count(when(col(c).contains('None') | \
              col(c).contains('NULL') | \
              (col(c) == '' ) | \
              col(c).isNull() | \
              isnan(c), c 
              )).alias(c)
          for c in df.columns])
df2.show()

