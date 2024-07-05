from kafka import KafkaConsumer
import json
import psycopg2
from .settings import settings

DATABASE_URL = settings.DATABASE_URL

# Kafka consumer configuration
consumer = KafkaConsumer(
    'todo_tasks',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Database connection
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Consuming messages
for message in consumer:
    task = message.value
    cur.execute("INSERT INTO task (task, notes, due_date) VALUES (%s, %s, %s)", 
                (task['task'], task['notes'], task['due_date']))
    conn.commit()

cur.close()
conn.close()
