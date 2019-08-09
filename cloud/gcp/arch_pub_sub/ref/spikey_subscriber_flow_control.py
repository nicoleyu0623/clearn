import time

from google.cloud import pubsub_v1

project_id = "spikey-ps"
subscription_name = "spikey_bug_report_sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    print('Received message: {}'.format(message.data))
    time.sleep(10)
    print("\n")
    message.ack()


flow_control = pubsub_v1.types.FlowControl(max_messages=5)


subscriber.subscribe(
    subscription_path, callback=callback, flow_control=flow_control)

print('Fetching messages on {}'.format(subscription_path))
while True:
    time.sleep(60)