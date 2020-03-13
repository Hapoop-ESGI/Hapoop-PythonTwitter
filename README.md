# Retrieve tweets in English and store them on the Hadoop Distributed File System (HDFS)

In order to mitigate the problem of classifying a large dataset that contains millions of _tweets_, we parallelize our work of classification of the tweets by working with the open source framework HADOOP, sharing the work of the storage and the parallelization between several machines in order to reduce the computation time. For that, we work with the __Hadoop Distributed File System (HDFS)__ to store the data set of tweets which we want to classify by using __SparkSession__, the entry point to programming Spark with the Dataset and DataFrame API:

```python
from pyspark.sql import SparkSession
```

we create the session,

```python
        self._spark_session = SparkSession.builder.appName("POOP").getOrCreate()
```

We assign the task of writing data to _hdfs_ to a single thread:

```python
    def write_data_hdfs(self, data):
```

In the _tweet_straming.py_ file, we define our main class:

```python
class StdOutListener(StreamListener)
```

which uses the methods defined above to continuously receive tweets from the stream, saves them to a json data file, and sends them to HDFS.
