from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType,StructField, StructType, ArrayType
import json


if __name__=="__main__" :
    spark = SparkSession.builder.appName("ResumeProcessing").getOrCreate()

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "INDEED") \
        .option("startingOffsets","earliest") \
        .load()
    

    
    lines = df.selectExpr("CAST(value AS STRING)")
    schema =StructType([StructField("companies", StringType(),True),
                           StructField("job_title", StringType(),True),
                           StructField("job_type",StringType(),True),
                           StructField("job_Description", StringType(),True),
                           StructField("job_link", StringType(),True),
                           ])
    data_lines = lines.select(from_json(col("value"), schema).alias("data")).select("data.*")
    data_agg_write_stream = data_lines \
        .writeStream \
        .trigger(processingTime='5 seconds') \
        .outputMode("append") \
        .option("truncate", "false") \
        .format("memory") \
        .queryName("jobPostTable") \
        .start()

    data_agg_write_stream.awaitTermination()

    


    
    