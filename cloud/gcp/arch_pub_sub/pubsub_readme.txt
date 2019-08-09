pluralsight pub/sub course

pub/sub   = message processing 

pub/sub  : complex pricing 

pub/sub == kafka == flink == SQS on AWS

pub/sub serverlesss, scales on few dimensions

topic= handshake betwen publisher and pub/sub
subscription = hadnshake between pub/sub and subscriber

publicsher apps create and send msgs on a Topic
subscriber apps subscribe to a topic to rcv messages

multiple subscribers can subscribe to topic and and least 1 subscriber needs
to ack a message to delete it


publisher <==many to many ==>  topic

subscriptions: push and pull
subscription <== multiple subscribers

if multiple subscribers use the same subscription they are not guaranteeed to 
receive all messages from subscription for ack

fan-in  fan-out  architectures

publishers and subscribers can be outsie gcp,  they need to access via https pub/sub urls. 