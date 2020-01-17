import json
import logging
import azure.functions as func
from graphene import Schema
from .helpers import responses
from .schema.Query import Query

def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Executing GraphQL function.')

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
            msg.set(message)

        return response
    else:
        return responses.bad_request(
            'Please pass a GraphQL query in the request body.')