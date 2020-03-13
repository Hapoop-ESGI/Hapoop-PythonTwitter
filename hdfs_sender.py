from threading import Thread
from pyspark.sql import SparkSession


class HDFSSender(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, data, hdfs_ip):
        Thread.__init__(self)
        self._data = data
        self._hdfs_ip = hdfs_ip
        self._spark_session = SparkSession.builder.appName("POOP").getOrCreate()

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        self.write_data_hdfs(self._data)

    def write_data_hdfs(self, data):
        rdd = self._spark_session.sparkContext.parallelize(data)
        rdd.saveAsTextFile(self._hdfs_ip)
