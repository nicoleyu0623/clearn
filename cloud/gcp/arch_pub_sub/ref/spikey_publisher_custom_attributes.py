import time
from google.cloud import pubsub_v1

project_id = "spikey-ps"
topic_name = "spikey_bug_report"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def callback(message_future):
    if message_future.exception(timeout=10):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())


for n in range(1, 10):
    data = u'Bug Reported Url: spikey.bug/xt1s{}'.format(n)
    data = data.encode('utf-8')
    
    message_future = publisher.publish(topic_path, data=data, branch='beta', username='Tester %d' % n)
    message_future.add_done_callback(callback)

print('Published List of Bugs with IDs:')


while True:
    time.sleep(10)