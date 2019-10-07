import json
import logging
import azure.functions as func
from mccore import Classifier

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('classify function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        classifier = Classifier.load_default()
        label, estimate = classifier.predict(name)
        return func.HttpResponse(json.dumps({
            "label": label,
            "confidence": estimate
        }),
        mimetype='application/json')
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )