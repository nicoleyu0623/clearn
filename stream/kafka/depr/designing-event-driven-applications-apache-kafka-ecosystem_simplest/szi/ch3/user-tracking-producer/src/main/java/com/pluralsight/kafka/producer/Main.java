package com.pluralsight.kafka.producer;


import com.pluralsight.kafka.producer.model.Event;
import lombok.extern.slf4j.Slf4j;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

import static java.lang.Thread.sleep;

@Slf4j
public class Main {

    public static void main(String[] args) throws InterruptedException {

        EventGenerator eventGenerator = new EventGenerator();

        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9093,localhost:9094");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<>(props);

        for(int i = 1; i <= 10; i++) {
            log.info("Generating event #" + i);

            Event event = eventGenerator.generateEvent();

            String key = extractKey(event);
            String value = extractValue(event);
            final String topic = "user-tracking";
            ProducerRecord<String, String> producerRecord = new ProducerRecord<>(topic, key, value);

            log.info("Producing to Kafka the record: " + key + ":" + value);
            producer.send(producerRecord); //sending to kafka

            sleep(1000);
        }

        producer.close();  //need to close connecton to kafka
    }

    private static String extractKey(Event event) {
        return event.getUser().getUserId().toString();
    }

    private static String extractValue(Event event) {
        return String.format("%s,%s,%s",
                event.getProduct().getType(),
                event.getProduct().getColor(),
                event.getProduct().getDesignType());
    }

}
