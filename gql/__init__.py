import logging
import os

from azure.storage.queue import QueueClient
from graphene import Schema

import azure.functions as func

from gql.helpers.context_builder import ContextBuilder
from gql.helpers.cache_manager import CacheManager
from gql.schema.Query import Query

import gql.helpers.responses as responses

CACHE_MANAGER = CacheManager(ContextBuilder())

def main(req: func.HttpRequest, cmdl: bytes, cvec: bytes, clbl: str, nmdl: bytes, guid: str) -> func.HttpResponse:
    logging.info('Executing GraphQL function.')

    queue = QueueClient.from_connection_string(os.environ['AzureWebJobsStorage'], 'predictions')

    try:
        query = req.get_body().decode()
    except ValueError:
        pass

    if query:
        schema = Schema(Query)
        context = CACHE_MANAGER.get(guid, cmdl, cvec, clbl, nmdl)
        results = schema.execute(query, context=context)
        response = responses.graphql(results)

        # Write response to azure queue storage
        message = responses.storage(results)
        if message:
            queue.send_message(message, time_to_live=-1)

        return response
    else:
        return responses.bad_request(
            'Please pass a GraphQL query in the request body.')
