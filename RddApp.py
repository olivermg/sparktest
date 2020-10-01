"""RddApp"""
from pyspark import SparkContext, SparkConf

def doubleAndSum(sc, data):
    distData = sc.parallelize(data)

    return distData.map(lambda n: n * 2).reduce(lambda s, n: s + n)

def run():
    conf = SparkConf().setAppName('RddApp').setMaster('local[4]')
    sc = SparkContext(conf=conf)

    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    doubleSum = doubleAndSum(sc, data)

    print("Sum of doubled values: %i" % doubleSum)

    sc.stop()

run()
