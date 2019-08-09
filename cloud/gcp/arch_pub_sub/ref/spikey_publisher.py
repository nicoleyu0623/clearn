from google.cloud import pubsub_v1

project_id = "spikey-ps"
topic_name = "spikey_bug_report"

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_name)

for n in range(1, 10):
   
    data = u'Bug Reported Url: spikey.bug/xt1s{}'.format(n)
    data = data.encode('utf-8')
    
    future = publisher.publish(topic_path, data=data)
    print('Published the list of bugs {} of  IDs {}.'.format(data, future.result()))

print('Published messages.')


#Change the name of the project and topic before recording 
#spikey-gcp to spikey-ps

