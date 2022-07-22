## CountingBykeys

```python
# Count the unique keys
total = Rdd.countByKey()

# What is the type of total?
print("The type of total is", type(total))
# Iterate over the total and print the output
for k, v in total.items(): 
  print("key", k, "has", v, "counts")

```

## Create a base RDD and transform it

The volume of unstructured data (log lines, images, binary files) in existence is growing dramatically, and PySpark is an excellent framework for analyzing this type of data through RDDs. In this 3 part exercise, you will write code that calculates the most common words from Complete Works of William Shakespeare.

```python

```
