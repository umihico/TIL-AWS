import boto3
import json
import ppickle
url=ppickle.load("../config.json")["sqs_name"]
sqs = boto3.resource('sqs')

body = {"type": "Right", "Action": "Ona"}
queue = sqs.get_queue_by_name(QueueName=url)
response = queue.send_message(
    MessageBody=json.dumps(body),)
import time
time.sleep(10)
queue = sqs.get_queue_by_name(QueueName=url)
for message in queue.receive_messages():
    print(json.loads(message.body))
    message.delete()
