import json
import logging
import os

from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential

import azure.functions as func


def main(event: func.EventGridEvent):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)
    #send_event(event)



# def send_event(event: func.EventGridEvent):
#     topic_key = os.environ["EVENTGRID_TOPIC_KEY"]
#     endpoint = os.environ["EVENTGRID_TOPIC_ENDPOINT"]

#     credential = AzureKeyCredential(topic_key)
#     client = EventGridPublisherClient(endpoint, credential)

#     client.send([ event ])