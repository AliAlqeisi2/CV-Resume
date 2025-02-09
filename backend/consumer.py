import json
from kafka import KafkaConsumer
from kafka.errors import KafkaError

# Kafka configuration
bootstrap_servers = "localhost:9092"
topic = "cv-views"
group_id = "cv-group"

# Create KafkaConsumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    auto_offset_reset="earliest",  # Start reading at the earliest message
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),  # Deserialize JSON
)

# Poll for messages
try:
    for message in consumer:
        print(f"Received event: {message.value}")

except KafkaError as e:
    print(f"Error consuming messages: {e}")

finally:
    # Close consumer
    consumer.close()