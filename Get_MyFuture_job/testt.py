import pandas as pd
companies= ["google", "binor"]
title=["stage", "first Job"]

string = {"companies":companies[0],"title":title[1]}
#print(string)

dataPost = pd.DataFrame()
dataPost["companies"]=companies
dataPost["job title"]=title
dataPost["job Type"]=title
dataPost["job Description"]=title
dataPost["job link"]=title


from kafka import KafkaProducer
from numpy import record
import pandas as pd
import json
print("Envoie des données vers kafka en cours...")



#data_list = data.to_dict(orient="records")


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

for i in range(len(dataPost)):
    message_to_kafka = {"companies":dataPost["companies"].iloc[i],"job_title":dataPost["job title"].iloc[i], "job_type":dataPost["job Type"].iloc[i],"job_Description":dataPost["job Description"].iloc[i],"job_link":dataPost["job link"].iloc[i]}
    print(message_to_kafka)
    data = json.dumps(message_to_kafka)
    print(data)
    publish_message(producer, 'test', data)

print("Kafka Producer Application Completed. ")

#, encoding='utf-8'