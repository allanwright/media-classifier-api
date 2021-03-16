import json
import azure.functions as func

def graphql(results):
    if results:
        res = {}
        if results.data:
            res['data'] = results.data
        if results.errors:
            res['errors'] = get_errors(results.errors)
        return func.HttpResponse(
            body=json.dumps(res),
            status_code=200)
    else:
        return bad_request('Unexpected error processing GraphQL request.')

def storage(results):
    try:
        return results.data['media']['name']
    except:
        return ''

def bad_request(message):
    return func.HttpResponse(
        body=json.dumps({
            "errors": [ get_error(message) ]
        }),
        status_code=400)

def get_errors(errors):
    return [
        get_error(e.message, get_locations(e.locations), e.path) for e in errors
    ]

def get_error(message, locations=None, path=None):
    return {
        "message": message,
        "locations": locations,
        "path": path
    }

def get_locations(locations):
    return [
        {"line": l.line, "column": l.column} for l in locations
    ]