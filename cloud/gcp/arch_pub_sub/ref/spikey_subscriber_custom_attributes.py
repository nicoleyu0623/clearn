import time
from google.cloud import pubsub_v1

project_id = "spikey-ps"
subscription_name = "spikey_bug_report_sub"

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    print('Received a Bug: {}'.format(message.data))
    if message.attributes:
        print('Attributes:')
        for key in message.attributes:
            value = message.attributes.get(key)
            print('{}: {}'.format(key, value))
    message.ack()


subscriber.subscribe(subscription_path, callback=callback)


print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)