import json
import logging
import os
import azure.functions as func
from azure.storage.queue import QueueClient
from graphene import Schema
from .helpers import responses
from .schema.Query import Query

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executing GraphQL function.')
    queue = QueueClient.from_connection_string(os.environ['AzureWebJobsStorage'], 'predictions')

    try:
        query = req.get_body().decode()
    except ValueError:
        pass

    if query:
        schema = Schema(Query)
        results = schema.execute(query)
        response = responses.graphql(results)

        # Write response to azure queue storage
        message = responses.storage(query, response)
        if message:
            queue.send_message(message, time_to_live=-1)

        return response
    else:
        return responses.bad_request(
            'Please pass a GraphQL query in the request body.')