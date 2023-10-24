from scrape_jobteaser import *
from kafka import KafkaProducer
from numpy import record
import pandas as pd
import json

# we jsonify the data 
data = data.to_json()
print(data)
def connect_kafka_producer():
    producer = None
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception lors de la connexion avec kafka', producer)
    finally:
        return producer
producer=connect_kafka_producer()

def publish_message(prod, topic_name, val):
    try:
        
        b_value = bytes(val, encoding='utf-8')
        
        prod.send(topic_name, value=b_value)
        prod.flush()
    except Exception as ex:
        print(str(ex))

publish_message(producer, 'jobTeaserInsa', json.dumps(data))

