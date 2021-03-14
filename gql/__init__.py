import json
import logging
import os
import azure.functions as func
from azure.storage.queue import QueueClient
from graphene import Schema
from .helpers import responses
from .schema.Query import Query

""" CACHE_MANANGER = CacheManager(ClassifierBuilder())
def main(req: func.HttpRequest, mdl: bytes, vec: bytes, lbl: str) -> func.HttpResponse:
    '''Gets the class of the specified filename.

    '''
    classifier = CACHE_MANANGER.get(vec, mdl, lbl)
    name = req.route_params['filename']
    prediction = classifier.predict(name)

    return func.HttpResponse(
        json.dumps(prediction),
        status_code=200,
        mimetype='application/json') """

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
        message = responses.storage(results)
        if message:
            queue.send_message(message, time_to_live=-1)

        return response
    else:
        return responses.bad_request(
            'Please pass a GraphQL query in the request body.')
