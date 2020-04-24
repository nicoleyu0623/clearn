#!/bin/bash

topic_name=viewrecords

#run to fetch events currently generated
#kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic ${topic_name} 

#replay all events stored in the topic
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic ${topic_name} --from-beginning 
