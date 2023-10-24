from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


if __name__=="__main__" :
    
    spark= SparkContext(appName="ResumeProcessing")
    sparkContext = StreamingContext(spark,30)
    kafka_msg = KafkaUtils.createDirectStream(sparkContext, topics=['sparkStreamingTest'],kafkaParams={'metadata.broker.list':'localhost:9092'})
    kafka_msg.pprint()

    sparkContext.start()
    sparkContext.awaitTermination()