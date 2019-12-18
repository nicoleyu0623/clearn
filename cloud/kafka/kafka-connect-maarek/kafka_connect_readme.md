# Apache kafka Connect hands-on Learning

## ch3 Kafka Connect Concepts
### Connect Architecture Design

```txt

        ||connect cluster|| ||kafka cluster||
=======    | worker |       | broker |  ->  [streams app1] 
Sources =>                              <-    
=======    | worker |       | broker |  ->  [streams app2]
                                        <-  
======     | worker |       | broker |  ->  [streams app3] 
Sinks   <=                              <-  
======     | worker |      | zookeeper |
```

Workers have (mutliple) tasks.

A task is a java process configured with a particular connector.

**Standalone** vs **distributed** mode
* standalone is easy and good for development
* distributed  is fault-tolerant
  * tasks can migrate from a failed host 

## ch4 setup and launch Kafka Connect Cluster

!w demo `/szi/dk_connect-cluster`

docker-compose.yml  has images for kafka cluster from 
docker image landoop/fast-data-dev with ports mapped:
* 2181 #zookeeper
* 3030 #landoop UI
* 8081-8083 #REST Proxy, schema registry, connect ports
* 9581-9585 #JMX Ports
* 9092:9092  # Kafka Broker

Other 2 images are for elasticsearch and for postgres

File `kafka-connect-tutorial-sources.sh`  is a script with step by step demo instructions
```
# Start our kafka cluster
docker-compose up kafka-cluster
```
goto landoo UI at  http://127.0.0.1:3030

Ctrl-C  to stop the kafka cluster

```
#to update  landoop docker image
docker pull landoop/fast-data-dev
```

`http://127.0.0.1:3030/logs/`  is a url to check cluster logs

Landoop docker image github repo
https://github.com/lensesio/fast-data-dev


###  source/demo-1  fileconnector standalone
from the folder szi/dk_connect-cluster  run another docker landoop image connecting to its shell 
```
docker run --rm -it -v "$(pwd)":/tutorial --net=host landoop/fast-data-dev:cp3.3.0 bash
```

```
# in the bash process of he landoop image /tutorial 
#is mapped to host's szi/dk_connect-cluster folder
# go to demo-1 folder
cd /tutorial/source/demo-1

#create topic  (#you can check it is created in landoo UI topics)
kafka-topics --create --topic demo-1-standalone --partitions 3 --replication-factor 1 --zookeeper 127.0.0.1:2181

# launch a connector with its config (part of kafka distribution)
connect-standalone worker.properties file-stream-demo-standalone.properties
```
`worker.properties` is first argument a worker konfing in standalone mode

`file-stream-demo-standalone.properties`  is a config about type of connector (FileStreamSourceConnector) witha param like source file=demo-file.txt  and a configured topic

Waite until you see in the Log output `INFO Created connector file-stream-demon-standalone ..`

Now write some lines in the file `demo-file.txt`

In Landoo topics UI you see those line as kafka messages in topic

Now stop the connector (Ctrl-C). 
* Obseve the creation of standalone.offsets file 

Now restart the connector  

Refresh the UI topic and observe nothing changed.  

Write an additional line in demo-file.txt   and see the new message arrive

### source/demo-2 fileconnector distributed

connector with enabled schema
```
#launch docker without mapping of current dir
docker run --rm -it  --net=host landoop/fast-data-dev:latest bash
#create new topic
kafka-topics --create --topic demo-2-distributed --partitions 3 --replication-factor 1 --zookeeper 127.0.0.1:2181
```

IN Landoo UI go to connectors, new connector.  Chose connector type __File__ .

this opens the config window for file connector

NB! in distributed mode one do not need a worker properties file