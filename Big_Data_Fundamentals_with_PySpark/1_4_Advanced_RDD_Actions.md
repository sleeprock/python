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
# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())

```
### Remove stop words and reduce the dataset
Remove stop words and reduce the dataset
After splitting the lines in the file into a long list of words in the previous exercise, in the next step, you'll remove stop words from your data. Stop words are common words that are often uninteresting. For example "I", "the", "a" etc., are stop words. You can remove many obvious stop words with a list of your own. But for this exercise, you will just remove the stop words from a curated list stop_words provided to you in your environment.

After removing stop words, you'll next create a pair RDD where each element is a pair tuple (k, v) where k is the key and v is the value. In this example, pair RDD is composed of (w, 1) where w is for each word in the RDD and 1 is a number. Finally, you'll combine the values with the same key from the pair RDD.

```python
# Convert the words in lower case and remove stop words from the stop_words curated list

splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1 
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

```

### Print word frequencies

After combining the values (counts) with the same key (word), in this exercise, you'll return the first 10 word frequencies. You could have retrieved all the elements at once using collect() but it is bad practice and not recommended. RDDs can be huge: you may run out of memory and crash your computer..

What if we want to return the top 10 words? For this, first you'll need to swap the key (word) and values (counts) so that keys is count and value is the word. After you swap the key and value in the tuple, you'll sort the pair RDD based on the key (count). This way it is easy to sort the RDD based on the key rather than the key using sortByKey operation in PySpark. Finally, you'll return the top 10 words from the sorted RDD.

You already have a SparkContext sc and resultRDD available in your workspace.

```python
# Display the first 10 words and their frequencies from the input RDD
for word in resultRDD.take(10):
	print(word)

# Swap the keys and values from the input RDD
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies from the sorted RDD
for word in resultRDD_swap_sort.take(10):
	print("{},{}".format(word[1], word[0]))

```
