import json
import logging
import azure.functions as func
from graphene import Schema
import gqllib.schema

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executing GraphQL function.')

    try:
        query = req.get_body().decode()
    except ValueError:
        pass

    if query:
        schema = Schema(gqllib.schema.Query)
        results = schema.execute(query)

        if results.errors:
            # TODO: Return errors in the proper format
            # https://graphql.org/learn/serving-over-http/#response
            return func.HttpResponse(
                results.errors[0].args[0],
                status_code=400)
        else:
            return func.HttpResponse(
                json.dumps(results.data),
                mimetype='application/json')
    else:
        return func.HttpResponse(
             "Please pass a GraphQL query in the request body.",
             status_code=400
        )