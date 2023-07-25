#JOIN in SPARK
Example 1: Left Join

A left join returns all the rows from the left DataFrame and the matching rows from the right DataFrame. 
If there is no match, the result will contain null values for the right DataFrame's columns.


# Perform a left join on "dept_id" column
left_joined_df = employees_df.join(departments_df, "dept_id", "left")

# Show the left joined DataFrame
left_joined_df.show()


Example 2: Right Join

A right join returns all the rows from the right DataFrame and the matching rows from the left DataFrame. 
If there is no match, the result will contain null values for the left DataFrame's columns.

# Perform a right join on "dept_id" column
right_joined_df = employees_df.join(departments_df, "dept_id", "right")

# Show the right joined DataFrame
right_joined_df.show()


Example 3: Cross Join

A cross join returns the Cartesian product of both DataFrames, 
which means all possible combinations of rows from both DataFrames.


# Perform a cross join
cross_joined_df = employees_df.crossJoin(departments_df)

# Show the cross joined DataFrame
cross_joined_df.show()


In this example, we use the 'crossJoin()' function to perform a cross join. 
The resulting DataFrame 'cross_joined_df' will contain all possible combinations of rows from 'employees_df' and 'departments_df'.
