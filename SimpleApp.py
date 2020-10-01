"""SimpleApp"""
from pyspark.sql import SparkSession
from os.path import expanduser

logFile = expanduser("~") + "/opt/spark/current/README.md"
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i lines with b: %i" % (numAs, numBs))

spark.stop()
