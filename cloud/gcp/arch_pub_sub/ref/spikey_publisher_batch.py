from google.cloud import pubsub_v1
import time


project_id = "spikey-ps"
topic_name = "spikey_bug_report"


batch_settings = pubsub_v1.types.BatchSettings(
    max_bytes=256,  # bytes
    max_latency=10,  # seconds
)
publisher = pubsub_v1.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project_id, topic_name)

    

for n in range(1, 100):
    data = u' New Bug - bug.io/{}'.format(n)
    data = data.encode('utf-8')   
    future = publisher.publish(topic_path, data=data)
    print('Published the list of bugs with ID {}.'.format(future.result()))

print('Published messages.')