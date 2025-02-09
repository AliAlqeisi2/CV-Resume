from kafka import KafkaProducer
import json
from datetime import datetime
from kafka.errors import KafkaError


def main ():
    kafka_config = {
        'bootstrap_servers' : "localhost:9092",
        'value_serializer'  : lambda v : json.dumps(v).encode("utf-8"),
        'key_serializer'    : str.encode
    }

    producer = KafkaProducer(**kafka_config)
    topic = "resume_views"




    def log_cv_view(user_agent):
        try:
            # Structured data to send
            event = {
                "event_type": "cv_view",
                "timestamp": datetime.now().isoformat(),
                "user_agent": user_agent,
            }

            # Send message to Kafka with a key
            key = "view"  # Simple string key
            future = producer.send(topic, key=key, value=event)

            # Block until the message is sent (optional)
            future.get(timeout=10)
            print(f"Message sent: key={key}, value={event}")

        except KafkaError as e:
                print(f"Failed to send message: {e}")
        

    log_cv_view("Mozilla/5.0")  # Test the producer
    
if __name__ == "__main__":
    main()
 


