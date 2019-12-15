# designing even-drive applications using Apache Kafka eco-system

## Plan
* ch1 Overview
* ch2 Experience the impact of even-driven architecture
* ch3 building your first apache kafka app
* ch4 communicating messages structure
* ch5 building your first streaming app 
* ch6 building a streaming application
* ch7 transferring data with kafka connect
* ch8 integrating applications with Rest Services

## Chapters

### ch 2 experiencing the impact of even-driven architecture
Example use-case  is online shop with clothes items with automated processes around production, storage and selling of products.

Enterprise Software Architecture design patterns.

EDA (event-driven architecture)

benefits vs drawbacks

!!w demo event storming
* DDD domain driven design
* event storming workshop
  
### ch3 Building your first Kafka app

Kafka history: started at linkedin in 2010, 2017 apache kafka  v 1.0
Kafka developed in scala then switched back to java

kafka is fast:
* no serialization/deserialization
  * transformation in bytes (cpu + time)
* kafka uses 1 byte-encoding format
* zero copy mechanism (msg is stored on a hard-drive directly from a network card. It does not pass by  JVM Heap)
    * only for non TLS connections (not encrypted)
* kafka is beyond a messaging system, it is a distributed streaming platform.  
  * a streaming platform can be used as a message system by pub/sub pattern. 
  * can be used as a distributed repliacated fault-tolerant storage
  * Data processing as events occur (Real-time processing)


**Kafka Architecture**

* Zoookeper
  * it's a centralized service and configuration for all brokers
  * is connected to several brokers, forming a cluster

!!w demo kafka setup 
    * 1 zookeeper, 2 brokers on local machine


kafka distribution:

`bin` has
* `kafka-server-{start|stop}.sh` 
*  `zookeper-server-{start|stop}.sh`
* `kafka-console-{consumer|producer|.sh}`
* `kafka-topics.sh`  

`config` has
* `server.properties`
* `zookeeper.properties`
* `{producer|consumer}.properties`
 
`../site-docs`   a folder with doc


demo kafka cluster config:
* zookeeper: 2181  in  `config/zookepr.properties`
* `cp config/server.properties config/server-1.properties`
  * `broker.id=1`
  * `listeners=PLAINTEXT://:9093`
  * `log.dirs=/tmp/kafka-logs-1`
* `cp config/server.properties config/server-2.properties`
    * `broker.id=2`
  * `listeners=PLAINTEXT://:9094`
  * `log.dirs=/tmp/kafka-logs-1`
  
starting:
* bin/zookeeper-server-start.sh
* bin/kafka-server-start.sh

NB! set up a docker-compose  with 1 zookeper and 2 brokers in folder

`infra/tech/docker-compose/zk-single-kafka-double`  

yml file : zk-single-kafka-double.yml

broker1 on port 9093  broker2 on port 9094

cl: c3Topics

A record has: 
{key(any type), value(any type), timestamp}

**topic**

is a category of messages e.g. example of topics for online shop
* account
* cart
* payment

by default a broker stores messages for 7 days

Compaction topics ? 
* messages with keys
* if a new msg has the same key, it is upserted
  
Messages in the same topics are split on different cluster nodes in **partitions**

A unique message in a topic is stored only in 1 (one) partition of the topic. 

A default message allocation between topic partitions on different brokers is round robin to ensure an even load. 

Partitions are replicated across cluster brokers.  

e.g. if we have broker0 and broker1  with topic partition0 and partition1,  a node0 will also have a copy of partition1 and node1  a copy of partition0. 

! review partitions in maarek course.

!!w  demo kafka producer 

maven proj path `szi/ch3/user-tracking-producer`

first create a topic `user-tracking`
```
kafka-topics --bootstrap-server localhost:9093 --partitions 2 or 1 --replication-factor 2 --topic user-tracking --create
```
check if topic was created, and describe it 
```
kafka-topics --bootstrap-server localhost:9093 --list

kafka-topics --bootstrap-server localhost:9093 --topic user-tracking --describe
```

Then in the maven project user-tracking-producer, compile it and run the Main class.
It will generate 10 messages 

Kafka consumer

kafka consumer is a **pull** mechanism. Pulling allows slow consumers not to block kafka cluster. 
* consumer continuously asks (every couple of ms) to check if there are new messages. 


!!w demo  user-tracking-consumer

path `szi/ch3/user-tracking-consumer`

Main has group.id specified in props on a consumer side. group.id is used when we want to share messages from the same topic across multiple consumers without having to deal with duplicate messages. Those multiple consumers will act as a sngle consumer

Message groups are out of this course scope. review mareek course.

demo: SuggestionEngine class does not have a concrete implementation, values are hard coded. 

Run the main class  to start the consumeer, then rerun the producer main class  and observe the consumption of messages. 

## ch 4 Communcationg messages structure

#### Serialization formats
* text encoded
  * json
  * xml (with optional schema)
  * yaml
* binary
  * avro with schemas
  * protobuf
  * thrift
  

