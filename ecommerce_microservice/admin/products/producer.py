import json
import pika
from dotenv import load_dotenv
import os


load_dotenv()
connection = pika.BlockingConnection(pika.URLParameters(os.getenv('pika_url')))
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key='main', body=json.dumps(body), properties=properties)
